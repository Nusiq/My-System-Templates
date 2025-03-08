Template project for dynamic world.

## Workflow
This project uses Regolith and System Tempalte. The template asks you to provide some information when it's initialzed. 

Project implements namespaceing based on System Template global replacements feature.

Regolith configuration contains multiple profiles:
- `default` - for the regular `regolith install` command.
- `publish` - creates a `releases/release.mctemplate` file.

The `_start` and `_end` profiles are shared between all profiles and shouldn't be ran directly.


The code-workspace file that ends with "debug" in its name is for debugging purposes with Minecraft Debugger VSCode extension. After compiling the project with regolith, you should be able to use that workspace to debug your code by pressing F5.
