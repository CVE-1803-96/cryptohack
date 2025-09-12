#!/usr/bin/env python3
from Crypto.Util.number import *

def main():
    """Main function - your code goes here"""
    
    long_n  = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
    byte_n  = long_to_bytes(long_n)
    print(byte_n)
        
    
    return 0

if __name__ == "__main__":
    main()