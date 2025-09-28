#!/usr/bin/env python3

from typing import ByteString, Optional, List, Tuple
from dataclasses import dataclass
import math
import re


@dataclass
class Candidate:
    key: bytes
    plaintext: bytes
    score: int
    prob: float



PRINTABLE_MIN = 32  # ' '
PRINTABLE_MAX = 126 # '~'
FLAG_PATTERN = re.compile(rb"^crypto\{[A-Za-z0-9_]+\}$")


COMMON_WORDS = [
    b"crypto", b"know", b"you", b"enough", b"with", b"this", b"flag", b"all", b"ctf",
    b"key", b"xor", b"secret", b"challenge", b"solve", b"brute", b"guess"
]


def is_printable_byte(b: int) -> bool:
    return PRINTABLE_MIN <= b <= PRINTABLE_MAX


def is_printable(data: ByteString) -> bool:
    return all(is_printable_byte(x) for x in data)


def xor(data: ByteString, key: ByteString) -> bytes:
    klen = len(key)
    return bytes(data[i] ^ key[i % klen] for i in range(len(data)))


def recover_known_key_bytes(ciphertext: ByteString, known_plaintext: ByteString, key_len: int) -> bytearray:
    """
    Recover key bytes at positions hit by the known prefix.
    """
    key = bytearray([0] * key_len)
    for i in range(min(len(known_plaintext), len(ciphertext))):
        key[i % key_len] = ciphertext[i] ^ known_plaintext[i]
    return key


def anchor_last_brace(ciphertext: ByteString, key: bytearray) -> None:
    """
    Anchor the key so the plaintext ends with '}'.
    """
    if not ciphertext or not key:
        return
    pos = (len(ciphertext) - 1) % len(key)
    key[pos] = ciphertext[-1] ^ ord("}")


def global_score(plaintext: bytes) -> int:

    
    if any(not is_printable_byte(b) for b in plaintext):
        return -10_000

    score = 0

   
    if FLAG_PATTERN.match(plaintext):
        score += 10_000

    
    for b in plaintext:
        if 65 <= b <= 90 or 97 <= b <= 122:      
            score += 3
        elif 48 <= b <= 57:                      
            score += 2
        elif b in (ord("_"), ord("{"), ord("}")):
            score += 2
        elif b in (ord(" "), ord("-"), ord("."), ord(","), ord("'")):
            score += 1

 
    lower = plaintext.lower()
    for w in COMMON_WORDS:
        if w in lower:
            score += 50

    
    score += len(plaintext)
    return score


def infer_position_candidates(
    ciphertext: ByteString,
    partial_key: bytearray,
    known_prefix: ByteString,
    pos: int
) -> List[Tuple[int, int]]:
   
    bests: List[Tuple[int, int]] = []
    original = partial_key[pos]

    bests.reserve if hasattr(bests, "reserve") else None  

    for candidate in range(256):
        partial_key[pos] = candidate
        plaintext = xor(ciphertext, partial_key)

      
        if not plaintext.startswith(known_prefix):
            continue

        s = global_score(plaintext)
        bests.append((candidate, s))

    
    partial_key[pos] = original

    
    bests.sort(key=lambda x: x[1], reverse=True)
    return bests


def infer_missing_keys_ranked(
    ciphertext: ByteString,
    partial_key: bytearray,
    known_prefix: ByteString,
    max_branch: int = 8
) -> List[bytes]:
  
    key_len = len(partial_key)
    covered_positions = set(i % key_len for i in range(len(known_prefix)))


    positions = list(range(key_len))
    positions.sort(key=lambda pos: -sum(1 for i in range(pos, len(ciphertext), key_len)))

    
    beam: List[bytearray] = [partial_key.copy()]

    for pos in positions:
        if pos in covered_positions:
            continue

       
        expanded: List[Tuple[bytearray, int]] = []
        for key_guess in beam:
            candidates = infer_position_candidates(ciphertext, key_guess, known_prefix, pos)
           
            for cand_byte, cand_score in candidates[:max_branch]:
                new_key = key_guess.copy()
                new_key[pos] = cand_byte
                
                pt = xor(ciphertext, new_key)
                expanded.append((new_key, global_score(pt)))

       
        if not expanded:
            return []

        
        expanded.sort(key=lambda kv: kv[1], reverse=True)
        beam = [kv[0] for kv in expanded[:max_branch]]

 
    return [bytes(k) for k in beam]


def softmax(scores: List[int], temperature: float = 1.0) -> List[float]:
    if not scores:
        return []
 
    m = max(scores)
    exps = [math.exp((s - m) / max(temperature, 1e-6)) for s in scores]
    total = sum(exps)
    return [e / total for e in exps]


def crack_ranked(
    ciphertext: ByteString,
    known_prefix: ByteString,
    min_key_len: int = 2,
    max_key_len: int = 32,
    top_n: int = 10
) -> List[Candidate]:
    
    all_candidates: List[Candidate] = []

    for key_len in range(min_key_len, max_key_len + 1):
        base_key = recover_known_key_bytes(ciphertext, known_prefix, key_len)
        anchor_last_brace(ciphertext, base_key)

       
        keys = infer_missing_keys_ranked(ciphertext, base_key, known_prefix, max_branch=8)
        for key in keys:
            plaintext = xor(ciphertext, key)

           
            if not plaintext.startswith(known_prefix):
                continue
            if not is_printable(plaintext):
                continue
            if b"}" not in plaintext[len(known_prefix):]:
                continue

            score = global_score(plaintext)
            all_candidates.append(Candidate(key=key, plaintext=plaintext, score=score, prob=0.0))

    
    all_candidates.sort(key=lambda c: c.score, reverse=True)

    
    probs = softmax([c.score for c in all_candidates], temperature=0.5)
    for c, p in zip(all_candidates, probs):
        c.prob = p

    return all_candidates[:top_n]


def main() -> None:
    CIPHERTEXT_HEX = (
        "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
    )
    ciphertext = bytes.fromhex(CIPHERTEXT_HEX)
    known_prefix = b"crypto{"

    candidates = crack_ranked(ciphertext, known_prefix, min_key_len=2, max_key_len=16, top_n=10)
    if not candidates:
        print("[-] No valid candidates found.")
        return

    print(f"[+] Found {len(candidates)} candidate(s):")
    for i, c in enumerate(candidates, 1):
        pt = c.plaintext.decode("utf-8", errors="replace")
        print(f"{i:2d}. Key={c.key!r}  Prob={c.prob:.3f}  Score={c.score}  Text={pt}")


if __name__ == "__main__":
    main()
