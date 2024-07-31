#include <iostream>
#include <string>

int main() {
    std::string hex;
    std::cout << "Enter hexadecimal value: ";
    std::cin >> hex;

    // Convert hexadecimal to ASCII
    for (size_t i = 0; i < hex.length(); i += 2) {
        std::string byte = hex.substr(i, 2);
        char c = static_cast<char>(std::stoi(byte, nullptr, 16));
        std::cout << c;
    }
    std::cout << std::endl;

    return 0;
}
