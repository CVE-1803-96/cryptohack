
#!/usr/bin/env python3
from typing import ByteString


def crack(c: ByteString) -> bytes:
    for key in range(256):
        k = key.to_bytes(1, byteorder='big')
        p = bytes(c[i] ^ k[i % len(k)] for i in range(len(c)))
        if b"crypto{" in p:
            return (k, p)
    return b""


def main() -> None:
    CIPHERTEXT = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
    plaintext = crack(CIPHERTEXT)
    if plaintext:
        print(f"[+] The favorite byte is: {plaintext[0]} ")
        print(f"[+] Found plaintext: {plaintext[1].decode('utf-8', errors='replace')}")
    else:
        print("[-] Plaintext not found")


if __name__ == "__main__":
    main()
      
# crypto{0x10_15_my_f4v0ur173_by7e}