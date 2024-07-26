#include <iostream>
#include <vector>

int main() {
    std::vector<int> ords = {81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79};
    int key = 0x32; // The XOR key

    std::cout << "Here is your flag:\n";
    for (int o : ords) {
        char decrypted = o ^ key;
        std::cout << decrypted;
    }

    return 0;
}
