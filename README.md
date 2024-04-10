[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/nfa-vfxim/tk-nuke?include_prereleases)](https://github.com/nfa-vfxim/tk-nuke) 
[![GitHub issues](https://img.shields.io/github/issues/nfa-vfxim/tk-nuke)](https://github.com/nfa-vfxim/tk-nuke/issues) 


# ShotGrid Engine for Nuke <img src="icon_256.png" alt="Icon" height="24"/>

ShotGrid Integration in Nuke

## Requirements

| ShotGrid version | Core version | Engine version |
|------------------|--------------|----------------|
| -                | v0.19.18     | -              |

## Configuration

### Booleans

| Name                       | Description                                                                                                                                 | Default value |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| `automatic_context_switch` | Controls whether Toolkit should attempt to automatically adjust its context every time the currently loaded file changes. Defaults to True. | True          |
| `debug_logging`            | Controls whether debug messages should be emitted to the logger                                                                             | False         |
| `use_sgtk_as_menu_name`    | Optionally choose to use 'Sgtk' as the primary menu name instead of 'ShotGrid'                                                              | False         |


### Lists

| Name                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Default value |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| `launch_builtin_plugins`   | Comma-separated list of tk-nuke plugins to load when launching Nuke. Use of this feature disables the classic mechanism for bootstrapping Toolkit when Nuke is launched.                                                                                                                                                                                                                                                                                                                                                                        | []            |
| `bin_context_menu`         | Controls which apps are added to the context menu for the bin view. This is a list and each item is a dictionary with keys app_instance, keep_in_menu, requires_select, and name. The app_instance parameter connects this entry to a particular app instance defined in the environment configuration file. The name is a menu name to add to the context menu. keep_in_menu is true if this item should be added to the main menu or not. requires_selection will disable the menu item when there are no items selected in the view.         | []            |
| `timeline_context_menu`    | Controls which apps are added to the context menu for the timeilne view. This is a list and each item is a dictionary with keys app_instance, keep_in_menu, requires_select, and name. The app_instance parameter connects this entry to a particular app instance defined in the environment configuration file. The name is a menu name to add to the context menu. keep_in_menu is true if this item should be added to the main menu or not. requires_selection will disable the menu item when there are no items selected in the view.    | []            |
| `spreadsheet_context_menu` | Controls which apps are added to the context menu for the spreadsheet view. This is a list and each item is a dictionary with keys app_instance, keep_in_menu, requires_select, and name. The app_instance parameter connects this entry to a particular app instance defined in the environment configuration file. The name is a menu name to add to the context menu. keep_in_menu is true if this item should be added to the main menu or not. requires_selection will disable the menu item when there are no items selected in the view. | []            |
| `favourite_directories`    | Adds entries to the favourites section in the file chooser.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | []            |
| `menu_favourites`          | Controls the favourites section on the main menu. This is a list and each menu item is a dictionary with keys app_instance and name. The app_instance parameter connects this entry to a particular app instance defined in the environment configuration file. The name is a menu name to make a favourite. An optional hotkey parameter can be included for triggering the menu action (Nuke only).                                                                                                                                           | []            |


### Strings

| Name                     | Description                                                                                                                                                                                                                                                                                                                                                   | Default value            |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| `project_favourite_name` | Allows customizing the name of the favourite directory representing the current project root in the file chooser. eg. 'ShotGrid Current Project'. In multi-root configs, there will be an entry for each root eg. 'ShotGrid Current Project (secondary)'. Specifying an empty string will disable this menu from being added to the favourites automatically. | ShotGrid Current Project |


### Integers

| Name                               | Description                                                                                                                                                                                                                                                                   | Default value |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| `compatibility_dialog_min_version` | Specify the minimum Application major version that will prompt a warning if it isn't yet fully supported and tested with Toolkit.  To disable the warning dialog for the version you are testing, it is recommended that you set this value to the current major version + 1. | 10            |


