Template project for dynamic world.

## Workflow
This project uses Regolith and System Tempalte. The template asks you to provide some information when it's initialzed. 

Project implements namespaceing based on System Template global replacements feature.

Regolith configuration contains multiple profiles:
- `default` - for the regular `regolith install` command.
- `debug` - for running with `F5` in VS Code to debug scripting. In addition to everything that `default` does it copies the files into `script_debug` folder and creates their source maps.
- `publish` - creates a `releases/release.mctemplate` file.

The `_start` and `_end` profiles are shared between all profiles and shouldn't be ran directly.

