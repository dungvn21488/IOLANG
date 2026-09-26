import os
import shutil

filecanbuild = "iolang™.py"

os.system(
    f"python3 -m pip install PyInstaller > {os.devnull} 2>&1"
)

os.system(
    f"python3 -m PyInstaller --onefile "
    f"--distpath . "
    f"--workpath ../build "
    f"--specpath ../ "
    f"--name iol "
    f"{filecanbuild} > {os.devnull} 2>&1"
)

shutil.rmtree("../build", ignore_errors=True)

specfile = "../iol.spec"

if os.path.exists(specfile):
    os.remove(specfile)