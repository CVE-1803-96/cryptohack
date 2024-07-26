#include <stdio.h>
#include <ctype.h>
#include <string.h>

void decryptCaesar(const char* ciphertext, int shift) {
    for (int key = 1; key <= 26; ++key) {
        char plaintext[1000] = {0};
        for (size_t i = 0; i < strlen(ciphertext); ++i) {
            char c = ciphertext[i];
            if (isalpha(c)) {
                char base = isupper(c) ? 'A' : 'a';
                char decrypted = base + (c - base - key + 26) % 26;
                plaintext[i] = decrypted;
            } else {
                plaintext[i] = c; // Non-alphabetic characters remain unchanged
            }
        }
        printf("Key %d output: %s\n", key, plaintext);
    }
}

int main() {
    char ciphertext[1000];
    printf("Enter the ciphertext: ");
    scanf("%s", ciphertext);

    decryptCaesar(ciphertext, 0); // Brute-force all keys
    return 0;
}
