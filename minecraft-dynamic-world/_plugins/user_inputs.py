import uuid

# Project Name
project_name = input("Project name (My Project): ") or "My Project"
project_name_dashes = project_name\
    .lower().replace(" ", "-").replace("_", "-").replace("'", "")
project_name_initials = "".join([i[0].lower() for i in project_name.split()])

# Author Name
author_name = input("Author name (Nusiq): ") or "Nusiq"
author_name_all_together = author_name\
    .lower().replace(" ", "").replace("-", "").replace("'", "")
author_name_all_together_plus_initials = author_name_all_together + "_" + project_name_initials

# Namespace
namespace_replacement_trigger = input(
    f"Namespace replacement trigger (@namespace): ") or "@namespace"
namespace_replacement_target = input(
    f"Namespace replacement value ({author_name_all_together_plus_initials}): ") or author_name_all_together_plus_initials

# Scripting
scripting_version = input("Scripting version, please check the most recent version manually (1.17.0): ") or "1.17.0"

# Base Game Version
base_game_version = input("Base game version, please check the most recent version manually (1.21.60): ") or "1.21.60"
base_game_version_list = [int(i) for i in base_game_version.split(".")]

# Update Packages?
update_packages = input("Update Regolith Packages and Install NPM Modules (y/N): ").lower() == "y"

# UUIDs
bp_uuid = str(uuid.uuid4())
rp_uuid = str(uuid.uuid4())
script_module_uuid = str(uuid.uuid4())
