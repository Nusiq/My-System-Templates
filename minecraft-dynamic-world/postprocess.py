import os

def print_red(text: str):
    print(f"\033[91m{text}\033[0m")

if update_packages:  # type: ignore
    os.chdir(__target__.parent)  # type: ignore
    os.system("regolith install-all -u")
    os.system("npm i")
else:
    print_red(
        "[WARNING] Skipped installing packages with 'regolith install-all -u' and 'npm i'.")
