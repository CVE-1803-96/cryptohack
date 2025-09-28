#!/usr/bin/env python3

def main():
    
    
    encode = bytes.fromhex("63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d")
    decode = "".join(chr(hex_code) for hex_code in encode)
    print(decode)
        
    
    return 0

if __name__ == "__main__":

    main()
