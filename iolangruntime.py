import sys
import os
import shutil
import platform
import time

importpath = []         
importpath_full = {}     
impy = []

io = False
os_ = False
time_ = False
path = False
var = []

imlib = ["io", "time", "os", "path"]

argv = sys.argv

if len(argv) == 1:
    print("is not file to run")
    sys.exit(1)

input_file = argv[1]

if input_file == "--version":
    print("IoLang™ runtime Version 1.000.05")
    print("Copyright © 2026 DungVN21488")
    sys.exit(0)

if len(argv) > 2:
    print("Runtime Error")
    sys.exit(1)

fopen = input_file
output = "a"

# Lấy thư mục chứa file .io
pathnow = os.path.dirname(os.path.abspath(fopen))
if not pathnow:
    pathnow = "."

# Quét file .ioh và .py trong cùng thư mục
for i in os.listdir(pathnow):
    full = os.path.join(pathnow, i)
    if os.path.isfile(full):
        if i.endswith(".ioh"):
            name = i[:-4]               # bỏ đuôi .ioh
            importpath.append(name)
            importpath_full[name] = full
        elif i.endswith(".py"):
            impy.append(i)

# Kiểm tra python3
pythony = shutil.which("python3") or shutil.which("python")

def install_python():
    system = platform.system()
    if system == "Windows":
        if shutil.which("winget"):
            return os.system(
                f'winget install --id Python.Python.3.14 -e --source winget > {os.devnull} 2>&1'
            )
        print("winget not found.")
    elif system == "Linux":
        if shutil.which("apt"):
            os.system("sudo apt update")
            return os.system(
                f"sudo apt install -y python3 python3-pip > {os.devnull} 2>&1"
            )
        if shutil.which("dnf"):
            return os.system(
                f"sudo dnf install -y python3 python3-pip > {os.devnull} 2>&1"
            )
        if shutil.which("pacman"):
            return os.system(
                f"sudo pacman -S --noconfirm python python-pip > {os.devnull} 2>&1"
            )
        print("No package manager found.")
    elif system == "Darwin":
        if shutil.which("brew"):
            return os.system(
                f"brew install python > {os.devnull} 2>&1"
            )
        print("Homebrew not found.")
    return 1

if not pythony:
    time.sleep(0.5)
    install_python()
    pythony = shutil.which("python3") or shutil.which("python")
    if not pythony:
        print("Python not found. Please install Python 3.")
        sys.exit(1)

# Mở file Python tạm
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

def compile(line):
    global io, os_, time_, path

    line = line.strip()
    if not line or line.startswith("#"):
        return

    if line.startswith("writeconsole "):
        content = line[len("writeconsole "):]
        printpy(f"print({content})\n")

    elif line.startswith("import "):
        importlib = line[len("import "):].strip()

        if importlib in imlib:
            if importlib == "io":
                io = True
            elif importlib == "os":
                os_ = True
                printpy("osname=os.name\n")
            elif importlib == "time":
                time_ = True
            elif importlib == "path":
                path = True
                printpy("pathnow=os.getcwd()\n")

        elif importlib in importpath:
            full_path = importpath_full[importlib]
            with open(full_path, "r", encoding="utf-8") as f:
                for i in f.read().splitlines():
                    compile(i)
        else:
            print("ImportError")
            sys.exit(1)

    elif line.startswith("input ") or line == "input":
        variable = line[len("input "):].strip() if line.startswith("input ") else ""
        if not variable:
            printpy("input()\n")
        elif variable in var:
            printpy(f"{variable}=input()\n")
        else:
            print("variable Not found")
            sys.exit(1)

    elif line.startswith("newreg "):
        reg = line[len("newreg "):].strip()
        printpy(f"{reg} = None\n")
        var.append(reg)

    elif line.startswith("output "):
        if not io:
            print(f"Error:{line} is invalid syntax")
            sys.exit(1)
        content = line[len("output "):]
        printpy(f"sys.stdout.write(str({content}))\n")
        printpy("sys.stdout.flush()\n")

    elif line.startswith("stderr "):
        if not io:
            print(f"Error:{line} is invalid syntax")
            sys.exit(1)
        content = line[len("stderr "):]
        printpy(f"sys.stderr.write(str({content}))\n")
        printpy("sys.stderr.flush()\n")

    elif line.startswith("mov "):
        content = line[len("mov "):]
        try:
            vari, value = content.split(",", 1)
        except ValueError:
            print(f"Error: MOV ERROR, invalid format")
            sys.exit(1)
        vari = vari.strip()
        value = value.strip()
        if vari in var:
            printpy(f"{vari}={value}\n")
        else:
            print(f"Error: MOV ERROR, {vari} is not a reg")
            sys.exit(1)

    elif line.startswith("wait "):
        if not time_:
            print(f"Error:{line} is invalid syntax")
            sys.exit(1)
        timewait = line[len("wait "):].strip()
        try:
            wait = int(timewait)
        except ValueError:
            print("ValueError")
            sys.exit(1)
        printpy(f"time.sleep({wait})\n")

    elif line in ["exit", "end", "quit"]:
        printpy("sys.exit()\n")

    elif line.startswith("$importpy "):
        imf = line[len("$importpy "):].strip()
        if imf in impy:
            full = os.path.join(pathnow, imf)
            with open(full, "r", encoding="utf-8") as f:
                for i in f.read().splitlines():
                    printpy(i + "\n")
        else:
            print(f"Error: Python file '{imf}' not found")
            sys.exit(1)

    elif line.startswith("system "):
        if not os_:
            print(f"Error:{line} is invalid syntax")
            sys.exit(1)
        command = line[len("system "):]
        printpy(f"os.system({command})\n")

    elif line.startswith("chdir "):
        if not path:
            print(f"Error:{line} is invalid syntax")
            sys.exit(1)
        cdpath = line[len("chdir "):]
        printpy(f"os.chdir({cdpath})\n")

    elif line.startswith("rmdir "):
        if not path:
            print(f"Error:{line} is invalid syntax")
            sys.exit(1)
        rmpath = line[len("rmdir "):]
        printpy(f"os.rmdir({rmpath})\n")

    elif line.startswith("const "):
        v = line[len("const "):]
        try:
            vari, value = v.split("=", 1)
        except ValueError:
            print(f"Error: invalid const syntax")
            sys.exit(1)
        printpy(f"{vari.strip()}={value.strip()}\n")

    elif line.startswith('pyexec "') and line.endswith('"'):
        coderun = line[len('pyexec "'):-1]
        printpy(coderun + "\n")

    else:
        print(f"Error: '{line}' is invalid syntax")
        sys.exit(1)

# Compile
try:
    with open(fopen, "r", encoding="utf-8") as f:
        for line in f.read().splitlines():
            compile(line)
except FileNotFoundError:
    print("FileNotFoundError")
    sys.exit(1)
finally:
    py.close()


exit_code = os.system(f"{pythony} {output}.py")


try:
    os.remove(f"{output}.py")
except OSError:
    pass

sys.exit(exit_code >> 8)