#include <stdio.h>
#include <ctype.h>

int main() {
    char *ciphertext = "QEXXIV IHMX PEOI AMRO";
    int shift;

    for (shift = 1; shift < 26; shift++) {
        char decrypted[100] = "";
        for (int i = 0; ciphertext[i] != '\0'; i++) {
            char char_to_decrypt = ciphertext[i];
            if (isalpha(char_to_decrypt)) {
                char base = isupper(char_to_decrypt) ? 'A' : 'a';
                char decrypted_char = (char_to_decrypt - base - shift + 26) % 26 + base;
                strncat(decrypted, &decrypted_char, 1);
            } else {
                strncat(decrypted, " ", 1);
            }
        }
        printf("Shift %d: %s\n", shift, decrypted);
    }

    return 0;
}
