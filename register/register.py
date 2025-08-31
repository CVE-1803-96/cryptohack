ciphertext = "QEXXIV IHMX PEOI AMRO"

for shift in range(1, 26):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += " "
    print(f"Shift {shift}: {decrypted}")