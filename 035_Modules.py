# Module:
    # A file containing code you want to include in your program
    # Use "import" to include a module (built-in or your own)
    # Useful to break up a large program reusable separate files

import math
print(math.pi)

import math as m
print(m.pi)

from math import pi
print(pi)

import TESTMODULE

print(TESTMODULE.square(2))
print(TESTMODULE.pi)