#!/usr/bin/env python3

import sys
# import this

def xor(a, b):
    r = []
    for i in range(len(a)):
        r.append(a[i] ^ b[i])
    return bytearray(r)

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

key1   = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
op1    = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
op2    = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
op3    = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
print("KEY1:", key1)

key2   = xor(key1, op1)
print("KEY2:", bytes(key2))
key3   = xor(key2, op2)
print("KEY3:", bytes(key3))
f1   =  xor(op3, key1) 
f2   =  xor(key2, key3)
flag =  xor(f1, f2) 
print("FLAG:", flag.decode('utf-8'))
