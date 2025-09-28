
#!/usr/bin/env python3
from typing import ByteString


def xor(a: ByteString, b: ByteString) -> bytes:
    if len(a) != len(b):
        raise ValueError("XOR requires equal-length byte strings.")
    return bytes(x ^ y for x, y in zip(a, b))


def main() -> None:
    
    
    FLAG_HEX = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"  # k1 xor k2 xor k3 xor flag
    K1_HEX   = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"  # k1
    K2X3_HEX = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"  # k2 xor k3

    
    k1     = bytes.fromhex(K1_HEX)
    k2_x3  = bytes.fromhex(K2X3_HEX)
    flag_x = bytes.fromhex(FLAG_HEX)

    # Compute k1 xor (k2 xor k3) = k1 xor k2 xor k3
    k1_x2_x3 = xor(k2_x3, k1)

    # Recover the flag: (k1 xor k2 xor k3 xor flag) xor (k1 xor k2 xor k3) = flag
    flag = xor(flag_x, k1_x2_x3)

    
    print(f"[+] k1 xor k2 xor k3: {k1_x2_x3.hex()}")
    print(f"[+] Flag: {flag.decode('utf-8', errors='replace')}")


if __name__ == "__main__":
    main()


# crypto{x0r_i5_ass0c1at1v3}