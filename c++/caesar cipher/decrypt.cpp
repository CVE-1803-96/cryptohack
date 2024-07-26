#include <iostream>
#include <string>

void decryptCaesar(const std::string& ciphertext, int shift) {
    for (int key = 1; key <= 26; ++key) {
        std::string plaintext;
        for (char c : ciphertext) {
            if (std::isalpha(c)) {
                char base = std::isupper(c) ? 'A' : 'a';
                char decrypted = base + (c - base - key + 26) % 26;
                plaintext += decrypted;
            } else {
                plaintext += c; // Non-alphabetic characters remain unchanged
            }
        }
        std::cout << "Key " << key << " output: " << plaintext << '\n';
    }
}

int main() {
    std::string ciphertext;
    std::cout << "Enter the ciphertext: ";
    std::cin >> ciphertext;

    decryptCaesar(ciphertext, 0); // Brute-force all keys
    return 0;
}
