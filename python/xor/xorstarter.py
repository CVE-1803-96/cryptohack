#!/usr/bin/env python3

import sys
from crypto.Util.number import *

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

label = input("Please enter the integer: ")
key   = int(input("please enter the key: "))
flag = "crypto{"
for c in label:
    val  = ord(c) ^ key
    flag = flag + str(chr(val))
flag = flag + "}"; 
#print the flag
print(flag)
