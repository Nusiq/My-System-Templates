THIS PROJECT WAS GENERATED USING THE [MINECRAFT DYNAMIC WORLD](https://github.com/Nusiq/My-System-Templates/tree/master/minecraft-dynamic-world) TEMPLATE.

# Features
- Automatic namespacing
- `.mctemplate` file generation for releases, with updated manifest versions based on Git tags
- Debugging support for the [Minecraft Bedrock Debugger VSCode extension](https://marketplace.visualstudio.com/items?itemName=mojang-studios.minecraft-debugger)

# About
## Namespacing
This project uses System Template to automatically generate namespaces using its [Global Replacements feature](https://system-template-docs.readthedocs.io/en/3.16.0/advanced_usage/replacements/#global-replacements).

This feature performs simple search-and-replace operations but is highly effective in most cases. Namespacing enhances system reusability, allowing you to copy and paste systems between projects without manual adjustments.

Instead of directly using your namespace in your systems (`filters_data/system_template/<your-system>`), use the `@namespace` keyword. For example, when creating an entity, use `@namespace:your_entity` instead of `your_namespace:your_entity`. The namespace is automatically replaced during compilation.

The project's [auto_map.json](https://system-template-docs.readthedocs.io/en/3.16.0/advanced_usage/custom_auto_mapping/#setting-up-the-auto-map-json-file) is configured to automatically namespace files that use their path as an identifier.

# Regolith Profiles
This project includes several preconfigured Regolith profiles:

- **default** – Used for development; compiles packs into the `com.mojang` development folders.
- **local_build** – Compiles files into the `build` folder, which is ignored by Git. This allows quick inspection of the generated files.
- **publish** – Creates a `.mctemplate` file in the `releases` folder. See the *Creating Releases* section for details.
- **_start** and **_end** – Internal profiles used by other profiles; should not be run directly.

# Creating Releases
You can generate `.mctemplate` files using the `publish` Regolith profile:

```
regolith run publish
```

This creates a `releases/<version>-release.mctemplate` file, where `<version>` is replaced with the latest Git tag (formatted as `X.X.X`).

The tags are also used to update all `"version"` properties in `manifest.json` files.

Additionally, running `publish` updates all version references in the `worlds/` folder. Since `worlds/` is not part of the Regolith project, this update is destructive. Commit changes to the `worlds/` folder after updating the versions.

# Code Workspace Files
The project includes two `.code-workspace` files:

- `<project-name>.code-workspace`
- `<project-name>-debug.code-workspace`

## Main Code Workspace
The main workspace, `<project-name>.code-workspace`, is used for regular development. You can build the project using:

```
regolith run
```
or
```
regolith watch
```

> [!WARNING]
> `regolith watch` does not detect changes in `local_modules`, as this folder is outside the Regolith project. See the *Esbuild Integration* section for details.

## Debug Code Workspace
The debug workspace is used to debug scripts in the project. Open `<project-name>-debug.code-workspace` in VSCode, then press `F5` to start debugging.

In Minecraft, run the following command to connect the debugger:

```
/script debugger connect
```

Note that you have to have the [Minecraft Bedrock Debugger VSCode extension](https://marketplace.visualstudio.com/items?itemName=mojang-studios.minecraft-debugger) installed for this to work.

# Esbuild Integration
The project includes certain workarounds to streamline development, though they come with some trade-offs.

## System Template and Local Node Modules
System Template enforces modularization, which can sometimes be limiting when multiple systems need to share code. While this isn't an issue for non-scripting workflows, scripting often benefits from a shared module for common utilities.

To address this, you can use the `local_modules` folder for custom Node modules. This folder is located outside the Regolith project, leading to both advantages and disadvantages:

Cons:
- `local_modules` cannot be watched by Regolith.
- The project cannot use [use_project_app_data_storage](https://regolith-docs.readthedocs.io/en/1.5.1/using-regolith/user-configuration/#use-project-app-data-storage-bool), as files must be compiled inside the project folder with access to local files.

Pros:
- Since `local_modules` is outside the Regolith project, it is not copied into a temporary folder during builds, resulting in faster compilation.
- Keeping shared modules in `local_modules` allows the Minecraft Debugger extension to access them directly, making it easier to set breakpoints and debug.

## Creating Local Modules
A basic Node module requires just two files:
- `package.json`
- `index.ts`

Place them inside `local_modules/<module-name>/`.

Here is an example:

`local_modules/demo-module/package.json`:
```json
{
	"name": "demo-module",
	"version": "1.0.0",
	"main": "index.ts"
}
```

`local_modules/demo-module/index.ts`
```typescript
import { world } from "@minecraft/server";

let helloCounter = 0;

export function printHello() {
	helloCounter++;
	world.sendMessage(`Hello ${helloCounter}`);
}
```

This module provides a simple `printHello` function that can be used across different systems within the project.
