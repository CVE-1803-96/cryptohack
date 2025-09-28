#!/usr/bin/env python3
from typing import ByteString


def xor(data: ByteString, key: ByteString) -> bytes:
    return bytes(data[i] ^ key[i % len(key)] for i in range(len(data)))


def main() -> None:
    
    plaintext = b"label"              # Directly use bytes instead of hex conversion
    key_value = 0x0D                  # XOR key as integer
    key = key_value.to_bytes(1, "big")

    result = xor(plaintext, key).decode("utf-8", errors="replace")
    print(f"crypto{{{result}}}")


if __name__ == "__main__":
    main()

# crypto{aloha}