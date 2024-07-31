#include <stdio.h>
#include <stdlib.h>

int main() {
    int key;
    char label[256]; // Assuming the label won't exceed 255 characters
    char flag[256]; // Assuming the flag won't exceed 255 characters
    int i;

    printf("Please enter the integer: ");
    fgets(label, sizeof(label), stdin);
    
    printf("please enter the key: ");
    scanf("%d", &key);

    flag[0] = 'c';
    flag[1] = 'r';
    flag[2] = 'y';
    flag[3] = 'p';
    flag[4] = 't';
    flag[5] = 'o';
    flag[6] = '{';
    
    for (i = 0; label[i] != '\0' && label[i] != '\n'; i++) {
        int val = (int)label[i] ^ key;
        flag[i + 7] = (char)val;
    }
    
    flag[i + 7] = '}';
    flag[i + 8] = '\0'; // Null-terminate the string

    // Print the flag
    printf("%s\n", flag);

    return 0;
}

