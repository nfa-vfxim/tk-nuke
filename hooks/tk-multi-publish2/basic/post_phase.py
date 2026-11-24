# Copyright (c) 2018 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import os

import sgtk
import nuke

HookBaseClass = sgtk.get_hook_baseclass()


class PostPhaseHook(HookBaseClass):
    """
    This hook defines methods that are executed after each phase of a publish:
    validation, publish, and finalization. Each method receives the publish
    tree instance being used by the publisher, giving full control to further
    curate the publish tree including the publish items and the tasks attached
    to them. See the :class:`PublishTree` documentation for additional details
    on how to traverse the tree and manipulate it.
    """

    # See the developer docs for more information about the methods that can be
    # defined here: https://developer.shotgunsoftware.com/tk-multi-publish2/
    def post_finalize(self, publish_tree):
        """
        This method is executed after the finalize pass has completed for each
        item in the tree.

        A :ref:`publish-api-tree` instance representing the items that were
        published and finalized is supplied as an argument. The tree can be
        traversed in this method to inspect the items and process them
        collectively.

        To glean information about the finalize state of particular items, you
        can iterate over the items in the tree and introspect their
        :py:attr:`~.api.PublishItem.properties` dictionary. This requires
        customizing your publish plugins to populate any specific finalize
        information that you want to process collectively here.

        .. warning:: You will not be able to use the item's
            :py:attr:`~.api.PublishItem.local_properties` in this hook since
            :py:attr:`~.api.PublishItem.local_properties` are only accessible
            during the execution of a publish plugin.

        :param publish_tree: The :ref:`publish-api-tree` instance representing
            the items to be published.
        """
        self.update_read_nodes(publish_tree)

    def update_read_nodes(self, publish_tree):
        """Point Read nodes at the publish location, but only for renders
        that were actually published in this session.

        Previously every ShotGrid write node was used, so Read nodes of write
        nodes that were left unchecked (or had nothing to publish) were also
        switched to a publish path that was never created.

        :param publish_tree: The publish tree that was just finalized.
        """
        published_paths = self._get_published_render_paths(publish_tree)
        if not published_paths:
            self.logger.debug("No write node renders published, Read nodes untouched.")
            return

        with nuke.root():
            for node in nuke.allNodes("Read"):
                read_path = node["file"].value()
                publish_path = published_paths.get(_normalize_path(read_path))
                if not publish_path:
                    continue

                node["file"].setValue(publish_path)
                self.logger.info(
                    "Updated %s to published path: %s" % (node.name(), publish_path)
                )

    def _get_published_render_paths(self, publish_tree):
        """Map the render paths published in this session to their publish
        paths.

        :param publish_tree: The publish tree that was just finalized.
        :returns: dict of normalized render path -> publish path
        """
        published_paths = {}

        for item in publish_tree:
            properties = item.properties

            # only ShotGrid write node renders that were registered in
            # ShotGrid this time (unchecked items never get sg_publish_data)
            if "sg_writenode" not in properties:
                continue
            if not properties.get("sg_publish_data"):
                continue

            render_path = properties.get("path")
            render_template = properties.get("work_template")
            publish_template = properties.get("publish_template")
            if not (render_path and render_template and publish_template):
                continue

            try:
                fields = render_template.get_fields(render_path)
                publish_path = publish_template.apply_fields(fields)
            except Exception as e:
                self.logger.warning(
                    "Could not resolve publish path for %s: %s" % (render_path, e)
                )
                continue

            publish_path = publish_path.replace(os.sep, "/")

            # never point a Read node at a folder that doesn't exist
            if not os.path.isdir(os.path.dirname(publish_path)):
                self.logger.warning(
                    "Publish folder missing, Read nodes not updated: %s"
                    % publish_path
                )
                continue

            published_paths[_normalize_path(render_path)] = publish_path

        return published_paths


def _normalize_path(path):
    """Normalize a path so slashes and (on Windows) case don't matter when
    comparing.
    """
    return os.path.normcase(os.path.normpath(path))
