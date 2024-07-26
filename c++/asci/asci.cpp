#include <iostream>

int main() {
    int ascii[] = {99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125};

    std::cout << "Here is your flag:\n";
    for (int c : ascii) {
        std::cout << static_cast<char>(c);
    }

    return 0;
}
