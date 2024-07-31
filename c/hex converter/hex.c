#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char hex[100];
    printf("Enter hexadecimal value: ");
    scanf("%s", hex);

    // Convert hexadecimal to ASCII
    int len = strlen(hex);
    for (int i = 0; i < len; i += 2) {
        char byte[3] = {hex[i], hex[i + 1], '\0'};
        printf("%c", (char)strtol(byte, NULL, 16));
    }
    printf("\n");

    return 0;
}
