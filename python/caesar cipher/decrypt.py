def decrypt_caesar(ciphertext):
    for key in range(1, 27):
        plaintext = ''
        for c in ciphertext:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                decrypted = chr(base + (ord(c) - base - key + 26) % 26)
                plaintext += decrypted
            else:
                plaintext += c  # Non-alphabetic characters remain unchanged
        print(f"Key {key} output: {plaintext}")

def main():
    ciphertext = input("Enter the ciphertext: ")
    decrypt_caesar(ciphertext)

if __name__ == "__main__":
    main()
