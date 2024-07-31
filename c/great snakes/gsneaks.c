#include <stdio.h>

int main() {
    int ords[] = {81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79};
    int key = 0x32; // XOR key

    printf("Here is your flag:\n");
    for (int i = 0; i < sizeof(ords) / sizeof(ords[0]); ++i) {
        printf("%c", ords[i] ^ key);
    }
    printf("\n");

    return 0;
}
