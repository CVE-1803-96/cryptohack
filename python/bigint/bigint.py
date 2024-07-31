#!/usr/bin/env python3

import sys
from crypto.Util.number import *

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

l = int(input("Please enter the integer: "))
b = long_to_bytes(l)
#unicode representation
print("Unicode representation of the integer: ", b.decode('utf-8'))
