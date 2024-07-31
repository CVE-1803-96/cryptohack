#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/bio.h>
#include <openssl/evp.h>

int main() {
    char hex[100];
    printf("Please enter your string here: ");
    scanf("%s", hex);

    // Convert hex string to binary data
    size_t len = strlen(hex);
    unsigned char* binData = (unsigned char*)malloc(len / 2);
    for (size_t i = 0; i < len; i += 2) {
        sscanf(hex + i, "%2hhx", &binData[i / 2]);
    }

    // Encode binary data to base64
    BIO* b64 = BIO_new(BIO_f_base64());
    BIO* bio = BIO_new(BIO_s_mem());
    BIO_push(b64, bio);
    BIO_write(b64, binData, len / 2);
    BIO_flush(b64);

    char* base64Data;
    BIO_get_mem_data(bio, &base64Data);

    printf("Base64-encoded data: %s\n", base64Data);

    // Clean up
    BIO_free_all(b64);
    free(binData);

    return 0;
}
