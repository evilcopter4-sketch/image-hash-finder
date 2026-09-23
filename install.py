import os
import sys
from pathlib import Path
import platform
import subprocess

curdr = Path(__file__).parent.resolve()
onedrive_desktop = Path.home() / "OneDrive" / "Desktop"

if onedrive_desktop.exists():
    top = onedrive_desktop
else:
    top = Path.home() / "Desktop"

# detecting OS
def detectos():
    system = platform.system()
    if system == "Windows":
        return "windows"
    elif system == "Linux":
        return "linux"
    else:
        sys.exit(f"Unsupported Operating System: {system} \nYou will have to compile the stuff yourself.")

#shortcut makers
def wshort(targcmd, name, targicon):
    shortpath = top / f"{name}.lnk"
    ps_script = f"""
    $WshShell = New-Object -ComObject WScript.Shell
    $Shortcut = $WshShell.CreateShortcut('{shortpath}')
    $Shortcut.TargetPath = '{targcmd}'
    $Shortcut.WorkingDirectory = '{curdr}'
    $Shortcut.IconLocation = '{targicon}'
    $Shortcut.Save()
    """
    
    #this bit will install the required modules for windows, hopefully. note that this file was made on a windows computer.
    #this is probably why it threw so many errors.
    subprocess.run(["pip", "install", "imagehash"], check=True)
    subprocess.run(["pip", "install", "pillow"], check=True)
    
    subprocess.run(["powershell", "-NoProfile", "-Command", ps_script], check=True)
    print(f"Created shortcut at: {shortpath}")

def lshort(targtrm, name, tarcon):
    shortpath = top / f"{name}.desktop"
    lindeskcont = f"""[Desktop Entry]
Type=Application
Terminal=true
Name={name}
Icon={tarcon}
Exec={targtrm}
"""

    try:
        subprocess.run(["sudo", "apt", "update", "-y"], check=True)
    except subprocess.CalledProcessError:
        print("sudo apt update failed. did you run this without sudo, and did you provide the correct password?")
        return
        
    subprocess.run(["pip", "install", "--user", "pillow"], check=True)
    subprocess.run(["pip", "install", "--user", "imagehash"], check=True)
    
    shortpath.write_text(lindeskcont)
    shortpath.chmod(0o755)
    print(f"succesfully created shortcut at {shortpath}")

#had to call this here so that the allfiles.append("wimagefind.cmd") would work
k = detectos()

#check if all files are present
allfiles = ["imagefind.py", "hashfind.ico"]
if k in ("windows", "Windows"):
    allfiles.append("wimagefind.cmd")

a_exist = [f for f in allfiles if (curdr / f).is_file()]
a_non_exist = list(set(a_exist) ^ set(allfiles))

print("existing: %s" % a_exist)            
print("non existing: %s" % a_non_exist)    
if a_non_exist:
    print("\nYou are missing some stuff:")
    print(f"\n{a_non_exist}")
    sys.exit(1)
 
# moving some stuff around
if k in ("windows", "Windows"):
    print("windows")
    wshort(
        targcmd=str(curdr / "wimagefind.cmd"),
        name="Image Hash finder",
        targicon=str(curdr /  "hashfind.ico")
        )
elif k in ("Linux", "linux"):
    print("Linux")
    lshort(
        targtrm=f"python3 {curdr / 'imagefind.py'}",
        name="Image Hash finder",
        tarcon=str(curdr / 'hashfind.ico')
        )

