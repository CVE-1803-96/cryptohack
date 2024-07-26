#include <iostream>
#include <string>

void encryptCaesar(const std::string& plaintext, int shift) {
    for (int key = 1; key <= 26; ++key) {
        std::string ciphertext;
        for (char c : plaintext) {
            if (std::isalpha(c)) {
                char base = std::isupper(c) ? 'A' : 'a';
                char encrypted = base + (c - base + key) % 26;
                ciphertext += encrypted;
            } else {
                ciphertext += c; // Non-alphabetic characters remain unchanged
            }
        }
        std::cout << "Key " << key << " output: " << ciphertext << '\n';
    }
}

int main() {
    std::string plaintext;
    std::cout << "Enter the plaintext: ";
    std::cin >> plaintext;

    encryptCaesar(plaintext, 0); // Brute-force all keys
    return 0;
}
