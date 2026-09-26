import sys
import os
import shutil
import platform
import time

importpath=[]
impy=[]


io = False
var = []

imlib = [
    "io",
    "time",
    "os",
    "path"
]

argv = sys.argv

if len(argv) == 1:
    print("is not file to build")
    sys.exit()

elif len(argv) >= 2:
    input_file = argv[1]

    if len(argv) == 2:
        if argv[1] == "--version":
            print("IoLang™ Version 1.000.05")
            print("Copyright © 2026 DungVN21488")
            sys.exit()
        else:
            fopen = input_file
            output = "a"

    elif len(argv) == 4:
        if argv[2] == "-o":
            output = argv[3]
            fopen = input_file
        else:
            print("building failed")
            sys.exit()

    else:
        print("building failed")
        sys.exit()
pathnow = os.path.dirname(os.path.abspath(fopen))
for i in os.listdir(pathnow):
    
    result=os.path.join(pathnow, i)
    if not(os.path.isdir(result)):
        if result.endswith(".ioh"):
            importpath.append(i)
            importpath.append(result)
            importpath.append(i[:-4])

for i in os.listdir(pathnow):
    
    result=os.path.join(pathnow, i)
    if not(os.path.isdir(result)):
        if result.endswith(".py"):
            impy.append(i)


print("Looking for Python...")

pythony = shutil.which("python3")
time.sleep(0.6)


def install_python():
    system = platform.system()

    if system == "Windows":
        if shutil.which("winget"):
            return os.system(
                "winget install --id Python.Python.3.14 -e --source winget"
            )

        print("winget not found.")

    elif system == "Linux":
        if shutil.which("apt"):
            os.system("sudo apt update")
            return os.system(
                "sudo apt install -y python3 python3-pip"
            )

        if shutil.which("dnf"):
            return os.system(
                "sudo dnf install -y python3 python3-pip"
            )

        if shutil.which("pacman"):
            return os.system(
                "sudo pacman -S --noconfirm python python-pip"
            )

        print("No package manager found.")

    elif system == "Darwin":
        if shutil.which("brew"):
            return os.system("brew install python")

        print("Homebrew not found.")

    return 1


if pythony:
    print("Python found")

else:
    print("Python not found")
    time.sleep(0.5)
    print("Downloading Python")
    install_python()


py = open(f"{output}.py", "w", encoding="utf-8")


def printpy(content):
    py.write(content)


printpy("import os, time, sys\n")
printpy(
    "Author='DungVN21488'\n"
    "version='1.000.05'\n"
    "true=True\n"
    "none=None\n"
    "false=False\n"

)

time_ = False
os_ = False
path=False


def compile(line):

    global io, os_, time_, path
    if path:
        printpy("pathnow=os.getcwd()\n")

    if not(line.strip()) or(line.startswith("#")):
        return 0

    if line.startswith("writeconsole "):

        content = line[len("writeconsole "):]

        printpy(f"print({content})\n")

    elif line.startswith("import "):

        importlib = line[len("import "):]

        if importlib in imlib:

            if importlib == "io":
                print(f"[INFO] importing module '{importlib}'")
                io = True

            if importlib == "os":
                print(f"[INFO] importing module '{importlib}'")
                os_ = True
                printpy("osname=os.name\n")

            if importlib == "time":
                print(f"[INFO] importing module '{importlib}'")
                time_ = True

            if importlib == "path":
                print(f"[INFO] importing module '{importlib}'")
                path=True
        elif importlib in importpath:
            if importlib.endswith(".ioh"):
                print(f"[INFO] importing file '{importlib}'")
            elif not(importlib.endswith(".ioh")):
                print(f"[INFO] importing '{importlib}'")
                importlib=importlib + ".ioh"
            with open(importlib, "r", encoding="utf-8") as f:
                for i in f.read().splitlines():
                    compile(i)

        else:

            print("ImportError")
            sys.exit()

    elif line.startswith("input ") or line == "input":

        variable = line[len("input "):].strip()

        if variable in var:

            printpy(f"{variable}=input()\n")

        elif not variable:

            printpy("input()\n")

        else:

            print("variable Not found")
            sys.exit()

    elif line.startswith("newreg "):

        reg = line[len("newreg "):]

        printpy(f"{reg} = None\n")

        var.append(reg)

    elif line.startswith("output "):

        if io:

            content = line[len("output "):]

            printpy(
                f"sys.stdout.write(str({content}))\n"
            )

            printpy(
                "sys.stdout.flush()\n"
            )

        else:

            print(
                f"Error:{line} is invalid syntax"
            )

            sys.exit()

    elif line.startswith("stderr "):

        if io:

            content = line[len("stderr "):]

            printpy(
                f"sys.stderr.write(str({content}))\n"
            )

            printpy(
                "sys.stderr.flush()\n"
            )

        else:

            print(
                f"Error:{line} is invalid syntax"
            )

            sys.exit()

    elif line.startswith("mov "):

        content = line[len("mov "):]

        vari, value = content.split(",", 1)

        vari = vari.strip()
        value = value.strip()

        if vari in var:

            printpy(
                f"{vari}={value}\n"
            )

        else:

            print(
                f"Error: MOV ERROR, {vari} is not a reg"
            )

            sys.exit()

    elif line.startswith("wait "):

        if time_:

            timewait = line[len("wait "):]

            try:
                wait = int(timewait)

            except ValueError:
                print("ValueError")
                sys.exit()

            printpy(
                f"time.sleep({wait})\n"
            )

        else:

            print(
                f"Error:{line} is invalid syntax"
            )

            sys.exit()

    elif line in ["exit", "end", "quit"]:

        printpy("sys.exit()\n")

    elif line.startswith("$importpy "):
        imf=line[len("$importpy "):]
        if imf in impy:
            
            with open(imf, "r", encoding="utf-8") as f:
                for i in f.read().splitlines():
                    printpy(i+"\n")


    elif line.startswith("system "):

        if os_:

            command = line[len("system "):]

            printpy(
                f"os.system({command})\n"
            )

        else:

            print(
                f"Error:{line} is invalid syntax"
            )

            sys.exit()

    elif line.startswith("chdir "):
        cdpath=line[len("chdir "):]
        if path:
            printpy(f"os.chdir({cdpath})\n")
        else:
            print(
                f"Error:{line} is invalid syntax"
            )
    elif line.startswith("rmdir "):
        rmpath=line[len("rmdir "):]
        if path:
            printpy(f"os.rmdir({rmpath})\n")
        else:
            print(
                f"Error:{line} is invalid syntax"
            )

    elif line.startswith("const "):
        v=line[len("const "):]
        vari, value=v.split("=", 1)
        value=value.strip()
        vari=vari.strip()
        printpy(f"{vari}={value}\n")

    elif line.startswith('pyexec "') and line.endswith('"'):
        coderun=line[len('pyexec "'):-1]
        printpy(coderun+"\n")
    else:

        print(
            f"Error: '{line}' is invalid syntax"
        )

        sys.exit()


try:

    with open(
        fopen,
        "r",
        encoding="utf-8"
    ) as f:

        code = f.read()

        for line in code.splitlines():

            print(
                f"[INFO] compile '{line}'"
            )

            time.sleep(0.2)

            compile(line)

except FileNotFoundError:

    print("FileNotFoundError")
    sys.exit()


py.close()

filecanbuild = f"{output}.py"

os.system(
    f"python3 -m pip install PyInstaller "
    f"> {os.devnull} 2>&1"
)

os.system(
    f"python3 -m PyInstaller "
    f"--onefile "
    f"--distpath . "
    f"--workpath ../build "
    f"--specpath ../ "
    f"{filecanbuild} "
    f"> {os.devnull} 2>&1"
)

shutil.rmtree(
    "../build",
    ignore_errors=True
)

if os.path.exists(
    f"../{output}.spec"
):

    os.remove(
        f"../{output}.spec"
    )

os.remove(filecanbuild)