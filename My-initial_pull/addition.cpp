#include <iostream>

int main() {
    int answer;
    int num1, num2, result;

    while (true) { // Infinite loop to keep asking
        std::cout << "Hello (1 for Yes, 0 for No): ";
        std::cin >> answer;

        if (answer == 1) {
            std::cout << "Hello, how are you...\n";
            
            std::cout << "Let's do some addition. Enter two numbers:\n";
            std::cout << "Number 1: ";
            std::cin >> num1;
            std::cout << "Number 2: ";
            std::cin >> num2;

            result = num1 + num2;
            std::cout << "The sum of " << num1 << " and " << num2 << " is " << result << ".\n";

        } else if (answer == 0) {
            std::cout << "Operation terminated. Exiting...\n";
            break; // Exit the loop and program
        } else {
            std::cout << "Invalid input. Try again.\n";
            break;
        }
    }

    return 0;
}
