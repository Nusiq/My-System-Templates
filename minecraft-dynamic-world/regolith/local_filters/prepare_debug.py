'''
Used in the 'debug' regolith profile to copy the script files and the source
map to the script_debug folder.
'''
import shutil
import os
import subprocess


bedrock_sid = "S-1-15-2-1958404141-86561845-1752920682-3514627264-368642714-62675701-733520436"
preview_sid = "S-1-15-2-424268864-5579737-879501358-346833251-474568803-887069379-4040235476"
loopback_exempt_command = "powershell CheckNetIsolation.exe LoopbackExempt -a -p="

if __name__ == '__main__':
    # Copy the script files
    regolith_project_path = os.environ['ROOT_DIR']
    shutil.rmtree(regolith_project_path + '/script_debug', ignore_errors=True)
    shutil.copytree('BP/scripts', regolith_project_path + '/script_debug', dirs_exist_ok=True)

    # Exempt for preview and bedrock
    subprocess.run(f'{loopback_exempt_command}{preview_sid}', shell=True)
    subprocess.run(f'{loopback_exempt_command}{bedrock_sid}', shell=True)
