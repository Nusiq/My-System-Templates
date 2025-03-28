# Minecraft Dynamic World Template
This is a project template for creating dynamic worlds in Minecraft using Regolith and System Template.

## Creating a New Project

If you have the [Regolith System Template](https://pypi.org/project/regolith-system-template/) tool installed and configured, you can create a new project in an empty directory by running:

```
system-template run minecraft-dynamic-world
```

This command will prompt you for additional information:
- **Project Name** – The name of the project, used for naming the behavior and resource packs, setting the `name` property in `config.json`, and naming the `.code-workspace` files. The name should be in Title Case (e.g., `My Project`). Spaces will be automatically replaced with underscores where necessary.
- **Author Name** – The author's name, stored in the `author` property of `config.json`.
- **Namespace Replacement Trigger** – A keyword used for namespace replacement, defaulting to `@namespace`. It is recommended to keep this default. More details about namespacing can be found in the [README](./regolith/README.md) file, which is automatically included in every generated project.
- **Namespace Replacement Value** – The value that will replace the `@namespace` keyword.
- **Scripting Version** – The version of the `@minecraft/server` module you want to use in the project.
- **Base Game Version** – The version for the project's manifest `base_game_version` property.
- **Update Regolith Packages and Install NPM Modules** – This is set to "no" by default. If set to "yes" (`y`), the project will automatically run `regolith install-all -u` and `npm i` after creation. This step is recommended, as the project may not run properly without it.

## Features
- Automatic namespacing
- `.mctemplate` file generation for releases, with updated manifest versions based on Git tags
- Debugging support for the [Minecraft Bedrock Debugger VSCode extension](https://marketplace.visualstudio.com/items?itemName=mojang-studios.minecraft-debugger)

For more details, refer to the [README](./regolith/README.md) file in the `regolith` folder, which is also automatically included in every generated project as the main README file.
