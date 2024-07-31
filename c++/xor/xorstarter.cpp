#include <iostream>
#include <string>

int main() {
    std::string label;
    int key;
    std::string flag = "crypto{";

    std::cout << "Please enter the integer: ";
    std::getline(std::cin, label);
    std::cout << "please enter the key: ";
    std::cin >> key;

    for (char c : label) {
        int val = static_cast<int>(c) ^ key;
        flag += static_cast<char>(val);
    }
    flag += "}";

    // print the flag
    std::cout << flag << std::endl;

    return 0;
}
