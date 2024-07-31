#!/usr/bin/env python3

import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

hex = input("Enter hexadecimal value: ")

print("Here is your flag:")
print(bytes.fromhex(hex).decode("utf-8"))
