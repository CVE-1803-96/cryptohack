#include <iostream>
#include <string>
#include <openssl/bio.h>
#include <openssl/evp.h>

int main() {
    std::string hex;
    std::cout << "Please enter your string here: ";
    std::cin >> hex;

    // Convert hex string to binary data
    size_t len = hex.length();
    std::vector<unsigned char> binData(len / 2);
    for (size_t i = 0; i < len; i += 2) {
        sscanf(hex.substr(i, 2).c_str(), "%2hhx", &binData[i / 2]);
    }

    // Encode binary data to base64
    BIO* b64 = BIO_new(BIO_f_base64());
    BIO* bio = BIO_new(BIO_s_mem());
    BIO_push(b64, bio);
    BIO_write(b64, binData.data(), len / 2);
    BIO_flush(b64);

    char* base64Data;
    BIO_get_mem_data(bio, &base64Data);

    std::cout << "Base64-encoded data: " << base64Data << std::endl;

    // Clean up
    BIO_free_all(b64);

    return 0;
}
