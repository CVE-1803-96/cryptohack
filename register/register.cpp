#include <iostream>
#include <string>

int main() {
    std::string ciphertext = "QEXXIV IHMX PEOI AMRO";

    for (int shift = 1; shift < 26; ++shift) {
        std::string decrypted = "";
        for (char char : ciphertext) {
            if (isalpha(char)) {
                int base = isupper(char) ? 'A' : 'a';
                decrypted += char((char - base - shift + 26) % 26 + base);
            } else {
                decrypted += " ";
            }
        }
        std::cout << "Shift " << shift << ": " << decrypted << std::endl;
    }

    return 0;
}
