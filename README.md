# IoLang™

**IoLang™ 1.000.05** — A lightweight programming language that compiles `.iol` source code into standalone Windows executables.

Created by **DungVN21488**.

## Features

* Simple `.iol` syntax
* Compile IoLang source into `.exe`
* Register variables with `newreg`
* Assign values with `mov`
* Define constants with `const`
* Console output with `writeconsole`
* User input with `input`
* Standard output and error output
* Delays with `wait`
* Execute system commands with `system`
* Directory operations with `chdir` and `rmdir`
* Direct Python execution with `pyexec`
* Import Python source files with `$importpy`
* Importable `.ioh` libraries
* Built-in `math.ioh`
* Python function integration
* UTF-8 source and generated Python support
* Automatic Python detection
* Automatic Python installation when required
* PyInstaller-based executable generation
* Custom executable names
* Dedicated IoLang runtime
* Windows installer
* IoLang uninstaller

## Installation

### Windows Installer

Download the IoLang setup package:

**[Download setup.zip](setup.zip)**

Extract `setup.zip`, then run:

```text
setup.exe
```

The installer:

1. Creates `C:\Program Files\IoLang`
2. Installs `iol.exe`
3. Installs `ior.exe`
4. Installs `iolang_delete.exe`
5. Adds IoLang to the system `PATH`
6. Makes `iol`, `ior`, and `iolang_delete` available from a new CMD or PowerShell window

After installation, open a **new** terminal and run:

```text
iol --version
```

Expected output:

```text
IoLang™ Version 1.000.05
Copyright © 2026 DungVN21488
```

You can also check the runtime:

```text
ior --version
```

Expected output:

```text
IoLang™ runtime Version 1.000.05
Copyright © 2026 DungVN21488
```

## Quick Start

Create a file named `main.iol`:

```iol
import io

newreg name
mov name, "DungVN21488"

writeconsole "Hello from IoLang™!"
writeconsole name
```

Compile it:

```text
iol main.iol
```

The compiler creates:

```text
a.exe
```

Run it:

```text
a.exe
```

## Custom Output Name

Use `-o` to specify the executable name:

```text
iol main.iol -o hello
```

This produces:

```text
hello.exe
```

## Variables

IoLang uses registers for mutable variables.

Create a register:

```iol
newreg name
```

Assign a value:

```iol
mov name, "DungVN21488"
```

Print it:

```iol
writeconsole name
```

Example:

```iol
newreg age
mov age, 12
writeconsole age
```

## Constants

Constants can be created with `const`:

```iol
const Pi = 3.141592653589793
const Name = "IoLang"
```

Constants are emitted directly into the generated Python program.

## Input

Input can be stored in a register:

```iol
newreg name
input name
writeconsole name
```

Standalone input is also supported:

```iol
input
```

## Modules

### `io`

Import:

```iol
import io
```

Console output:

```iol
output "Hello"
```

Standard error:

```iol
stderr "Error message"
```

### `time`

Import:

```iol
import time
```

Wait:

```iol
wait 1
```

The value is specified in seconds.

### `os`

Import:

```iol
import os
```

Execute a system command:

```iol
system "echo Hello"
```

### `path`

Import:

```iol
import path
```

Directory operations:

```iol
chdir "C:\\Users"
rmdir "C:\\Temp\\Example"
```

## `.ioh` Libraries

IoLang supports `.ioh` library files.

An `.ioh` file can contain IoLang code that is compiled into the current program.

Example:

```text
math.ioh
```

Import it with:

```iol
import math
```

or:

```iol
import math.ioh
```

For example, `math.ioh` can contain:

```iol
pyexec "import math"

const Pi = math.pi
const E = math.e
const Tau = math.tau
const Nan = math.nan
const Infi = math.inf
```

After importing:

```iol
import math

writeconsole Pi
writeconsole E
writeconsole Tau
writeconsole Nan
writeconsole Infi
```

Output:

```text
3.141592653589793
2.718281828459045
6.283185307179586
nan
inf
```

### Built-in `math.ioh`

IoLang includes a mathematics library:

```text
math.ioh
```

It provides:

```text
Pi
E
Tau
Nan
Infi
```

Download:

**[Download math.ioh](math.ioh)**

The `math.ioh` file should be treated as a library file and should not be modified unless you understand its contents.

## Python Integration

IoLang 1.000.05 can directly include Python source code in the generated Python program.

### `$importpy`

Use:

```iol
$importpy math_.py
```

The `.py` file must be available in the same directory as the IoLang source.

Example `math_.py`:

```python
def add(one, two):
    return one + two

def sub(one, two):
    return one - two
```

IoLang source:

```iol
import io
$importpy math_.py

output add(90, 80)
output "\n"
output sub(500, 100)
output "\n"
```

Output:

```text
170
400
```

The Python source is copied directly into the generated Python program.

This allows IoLang programs to use Python functions without requiring IoLang to implement those functions itself.

## `pyexec`

`pyexec` allows Python source code to be inserted directly into the generated Python program.

Example:

```iol
pyexec "import random"
```

Another example:

```iol
pyexec "print('Hello from Python')"
```

No `import python` statement is required.

## Comments

Lines beginning with `#` are treated as comments:

```iol
# This is a comment

writeconsole "Hello"
```

Blank lines are also ignored.

## Exit

IoLang supports:

```iol
exit
```

as well as:

```iol
end
```

and:

```iol
quit
```

## Runtime

IoLang includes a dedicated runtime executable:

```text
ior.exe
```

Check the runtime version:

```text
ior --version
```

Expected output:

```text
IoLang™ runtime Version 1.000.05
Copyright © 2026 DungVN21488
```

The runtime is installed to:

```text
C:\Program Files\IoLang\ior.exe
```

## Uninstaller

IoLang includes:

```text
iolang_delete.exe
```

The uninstaller is installed to:

```text
C:\Program Files\IoLang\iolang_delete.exe
```

It is included as part of the IoLang Windows installation.

## Compiler Pipeline

IoLang uses the following build pipeline:

```text
.iol
 │
 ▼
IoLang Compiler
 │
 ├── .ioh
 │
 └── .py
 │
 ▼
generated .py
 │
 ▼
PyInstaller
 │
 ▼
standalone .exe
```

For example:

```text
main.iol
   ↓
IoLang Compiler
   ↓
main.py
   ↓
PyInstaller
   ↓
a.exe
```

The generated Python source is temporary and is removed after the executable is built.

## Python Detection

IoLang automatically searches for Python.

The compiler reports:

```text
Looking for Python...
Python found
```

If Python is unavailable, IoLang can attempt to install Python 3.14 using an available package manager.

Supported package managers include:

* `winget`
* `apt`
* `dnf`
* `pacman`
* `brew`

## PyInstaller

IoLang automatically installs PyInstaller when required:

```text
python3 -m pip install PyInstaller
```

The executable is then generated using:

```text
python3 -m PyInstaller --onefile
```

## UTF-8

IoLang uses UTF-8 when reading source files and generating Python source code.

Unicode text such as:

```iol
writeconsole "IoLang™"
```

is supported.

## Requirements

For building IoLang programs:

* Python 3.14 or compatible Python installation
* PyInstaller
* Windows for the current executable build workflow

The IoLang compiler can automatically install PyInstaller when needed.

## Command Reference

| Command        | Description                               |
| -------------- | ----------------------------------------- |
| `newreg`       | Create a mutable register                 |
| `mov`          | Assign a value to a register              |
| `const`        | Define a constant                         |
| `writeconsole` | Print to the console                      |
| `input`        | Read user input                           |
| `output`       | Write to standard output                  |
| `stderr`       | Write to standard error                   |
| `wait`         | Wait for a number of seconds              |
| `system`       | Execute a system command                  |
| `chdir`        | Change the current directory              |
| `rmdir`        | Remove a directory                        |
| `pyexec`       | Inject Python source                      |
| `$importpy`    | Import Python source                      |
| `import`       | Import an IoLang module or `.ioh` library |
| `exit`         | Exit the program                          |
| `end`          | End the program                           |
| `quit`         | Quit the program                          |

## Project Files

```text
IoLang/
├── iolang™.py
├── iol.exe
├── ior.exe
├── iolang_delete.exe
├── setup.c
├── setup.exe
├── setup.zip
├── build.py
├── math.ioh
├── LICENSE
└── README.md
```

## Downloads

### Windows Installer

**[Download setup.zip](setup.zip)**

Contains the IoLang Windows installer and the required IoLang executables.

### Mathematics Library

**[Download math.ioh](math.ioh)**

The built-in mathematics library for IoLang.

## Version

**IoLang™ Version 1.000.05**

Created by **DungVN21488**

Copyright © 2026 DungVN21488

---

**IoLang™ 1.000.05 — Final Version**
