#!/usr/bin/env python3

import sys
import base64
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

hex = input("Please enter your string here: ")
# convert hex string to latin1 string
hex = bytes.fromhex(hex).decode("latin-1")
# encode latin1 string to base64 byte string
print(base64.b64encode(bytes(hex, 'latin-1')))
