#!/usr/bin/env python3
import base64

def main():
    
    
    bytes_code  = bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")
    base64_code = base64.b64encode(bytes_code)
    print(base64_code)
        
    
    return 0

if __name__ == "__main__":

    main()
