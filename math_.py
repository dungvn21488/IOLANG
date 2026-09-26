# math_.py - Math helper functions for IoLang
# Compatible with IoLang™ 1.000.05

import math

# === Basic arithmetic ===
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b if b != 0 else float("nan")

def mod(a, b):
    return a % b if b != 0 else float("nan")

def power(a, b):
    return a ** b

# === Common math functions ===
def sqrt(x):
    return math.sqrt(x)

def abs(x):
    return math.fabs(x)

def floor(x):
    return math.floor(x)

def ceil(x):
    return math.ceil(x)

def round(x):
    return math.round(x) if hasattr(math, "round") else __builtins__["round"](x)

# === Trigonometry (input in radians) ===
def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

# === Conversion ===
def to_deg(rad):
    return math.degrees(rad)

def to_rad(deg):
    return math.radians(deg)

# === Utility ===
def clamp(x, lo, hi):
    return max(lo, min(hi, x))

def min_val(a, b):
    return a if a < b else b

def max_val(a, b):
    return a if a > b else b