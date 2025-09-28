#!/usr/bin/env python3
"""
Per-pixel RGB XOR of two images.

Usage examples:
  python xor_images.py image1.png image2.png
  python xor_images.py image1.png image2.png --out result.png --show
"""

from pathlib import Path
from typing import Optional
from PIL import Image
import argparse


def xor_images(
        
) -> Path:
    path_a = Path("./flag.png")
    path_b = Path("./lemur.png")
    a = Image.open(path_a).convert("RGB")
    b = Image.open(path_b).convert("RGB")

    if a.size != b.size:
        raise ValueError(f"Image sizes differ: {a.size} vs {b.size}")

    buf_a = a.tobytes()
    buf_b = b.tobytes()

    if len(buf_a) != len(buf_b):
        raise RuntimeError("Unexpected: byte buffers differ in length after conversion to RGB")

    # XOR byte-by-byte into a mutable bytearray for speed
    out_buf = bytearray(len(buf_a))
    mv_a    = memoryview(buf_a)
    mv_b    = memoryview(buf_b)
    print(out_buf)
    print(mv_a)
    print(mv_b)
    for i in range(len(out_buf)):
        out_buf[i] = mv_a[i] ^ mv_b[i]

    result = Image.frombytes("RGB", a.size, bytes(out_buf))
    out_path = path_a.with_name(f"{path_a.stem}_xor_{path_b.stem}.png")
    result.save(out_path)
    result.show()
    
        

    return out_path





def main() -> None:
    
    out =   xor_images()
    print(f"[+] Saved XOR image to: {out}")

if __name__ == "__main__":
    main()


# crypto{X0Rly_n0t!}