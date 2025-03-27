import subprocess
import os

def get_version():
    try:
        # The repository path is stored in the ROOT_DIR variable
        root_dir = os.environ.get('ROOT_DIR')

        git_out = subprocess.check_output(
            'git describe --tags --always --abbrev=0',
            cwd=root_dir
        )
        git_out = git_out.decode('utf-8').splitlines()[0].strip()
        git_version = [*map(lambda x: int(x), git_out.split('.'))]
        return git_version
    except:
        text = "Unable to get project version from git tag. Using 1.0.0."
        print(f"\033[91m{text}\033[0m")  # red text
        return [1, 0, 0]

RELEASE_VERSION = get_version()
