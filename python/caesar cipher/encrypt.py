def encrypt_caesar(plaintext):
    for key in range(1, 27):
        ciphertext = ''
        for c in plaintext:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                encrypted = chr(base + (ord(c) - base + key) % 26)
                ciphertext += encrypted
            else:
                ciphertext += c  # Non-alphabetic characters remain unchanged
        print(f"Key {key} output: {ciphertext}")

def main():
    plaintext = input("Enter the plaintext: ")
    encrypt_caesar(plaintext)

if __name__ == "__main__":
    main()
