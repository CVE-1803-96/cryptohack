#include <iostream>
#include <vector>
#include <iomanip>
#include <sstream>

std::vector<uint8_t> xor_bytes(const std::vector<uint8_t>& a, const std::vector<uint8_t>& b) {
    std::vector<uint8_t> r;
    for (size_t i = 0; i < a.size(); ++i) {
        r.push_back(a[i] ^ b[i]);
    }
    return r;
}

std::vector<uint8_t> hex_to_bytes(const std::string& hex) {
    std::vector<uint8_t> bytes;
    for (size_t i = 0; i < hex.length(); i += 2) {
        std::string byteString = hex.substr(i, 2);
        uint8_t byte = static_cast<uint8_t>(strtol(byteString.c_str(), nullptr, 16));
        bytes.push_back(byte);
    }
    return bytes;
}

int main() {
    #ifdef __cplusplus
    std::cout << "You are running C++." << std::endl;
    #endif

    std::vector<uint8_t> key1 = hex_to_bytes("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313");
    std::vector<uint8_t> op1 = hex_to_bytes("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e");
    std::vector<uint8_t> op2 = hex_to_bytes("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1");
    std::vector<uint8_t> op3 = hex_to_bytes("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf");

    std::cout << "KEY1: ";
    for (auto byte : key1) {
        std::cout << std::hex << std::setw(2) << std::setfill('0') << (int)byte;
    }
    std::cout << std::endl;

    std::vector<uint8_t> key2 = xor_bytes(key1, op1);
    std::cout << "KEY2: ";
    for (auto byte : key2) {
        std::cout << std::hex << std::setw(2) << std::setfill('0') << (int)byte;
    }
    std::cout << std::endl;

    std::vector<uint8_t> key3 = xor_bytes(key2, op2);
    std::cout << "KEY3: ";
    for (auto byte : key3) {
        std::cout << std::hex << std::setw(2) << std::setfill('0') << (int)byte;
    }
    std::cout << std::endl;

    std::vector<uint8_t> f1 = xor_bytes(op3, key1);
    std::vector<uint8_t> f2 = xor_bytes(key2, key3);
    std::vector<uint8_t> flag = xor_bytes(f1, f2);

    std::cout << "FLAG: ";
    for (auto byte : flag) {
        std::cout << (char)byte;
    }
    std::cout << std::endl;

    return 0;
}

