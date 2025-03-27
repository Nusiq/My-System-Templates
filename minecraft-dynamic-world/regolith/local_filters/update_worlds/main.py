'''
Updates the manifests in the 'worlds' directory to match the version of the
project based on the git tag.
'''
from better_json_tools import load_jsonc, CompactEncoder
import json
from pathlib import Path
import subprocess
import os

def get_version() -> list[int]:
    try:
        git_out = subprocess.check_output('git describe --tags --always --abbrev=0')
        git_out = git_out.decode('utf-8').splitlines()[0].strip()
        git_version = [*map(lambda x: int(x), git_out.split('.'))]
        return git_version
    except:
        text = "Unable to get project version from git tag. Using 1.0.0."
        print(f"\033[91m{text}\033[0m")  # red text
        return [1, 0, 0]

def update_world_x_pack(path: Path, version: list[int]) -> str:
    json_walker = load_jsonc(path)
    for version_field in json_walker // int / "version":
        version_field.data = version
    return json.dumps(json_walker.data, cls=CompactEncoder)

def update_manifest(path: Path, version: list[int]) -> str:
    json_walker = load_jsonc(path)
    header_version_field = json_walker / "header" / "version"
    header_version_field.data = version
    for module_version_field in json_walker / "modules" // int / "version":
        module_version_field.data = version
    return json.dumps(json_walker.data, cls=CompactEncoder)

def main():
    root_dir = os.environ.get('ROOT_DIR')
    assert root_dir is not None, "ROOT_DIR environment variable is not set."
    os.chdir(root_dir)
    version = get_version()

    # Files to update. List all of the changes to apply to reduce the risk
    # of invalid state (this is still not perfect, but better than nothing).
    files_to_update: dict[Path, str] = {}
    for world in Path("worlds").glob("*"):
        if not world.is_dir():
            continue
        # world_behavior_packs.json & world_resource_packs.json
        wbp = world / "world_behavior_packs.json"
        files_to_update[wbp] = update_world_x_pack(wbp, version)
        wrp = world / "world_resource_packs.json"
        files_to_update[wrp] = update_world_x_pack(wrp, version)
        # manifest.json
        manifest = world / "manifest.json"
        files_to_update[manifest] = update_manifest(manifest, version)
    for file, content in files_to_update.items():
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)


if __name__ == "__main__":
    main()
