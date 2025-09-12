from pwn import * # pip install pwntools
import json
import codecs
from Crypto.Util.number import *

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def defeat_level(type_encode, code):
        data = ""
        if type_encode == "base64":
            data = base64.b64decode(code).decode() 
        
        elif type_encode == "hex":
            data = bytes.fromhex(code)
            data = data.decode("utf-8")

        elif type_encode == "rot13":
            data = codecs.decode(code, 'rot_13')

        elif type_encode == "bigint":
            data = long_to_bytes(int(code, 16))
            data = data.decode("utf-8")
            
        elif type_encode == "utf-8":
            data = "".join([chr(b) for b in code])

        return {"type": type_encode, "decoded": data}

#Defeating all 100's level
for level in range(100):
    print(f"LEVEL [{level}]:\n")
    received = json_recv()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])
    solve = defeat_level(received["type"], received["encoded"]) 
    to_send = {
                "decoded": solve["decoded"]   
            }
    print("Sending decoded value: ")
    print(solve["decoded"])
    json_send(to_send)
    
#The last call for the flag
json_recv()

