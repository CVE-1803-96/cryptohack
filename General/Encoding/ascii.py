#!/usr/bin/env python3

def main():
    """Main function - your code goes here"""
    
    encode = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
    decode = "".join(chr(ascii_code) for ascii_code in encode)
    print(decode)
        
    
    return 0

if __name__ == "__main__":
    main()