#include <stdint.h>
#include <stdbool.h>

bool isPalindrome(int number) {
    int digit;
    uint32_t tmp = number, reversed_number = 0;

    if (number < 0)
        return false;

    if (number == 0)
        return true;
  
    while (tmp > 0) {
        digit = tmp % 10;
        tmp /= 10;
        reversed_number = (reversed_number * 10) + digit;
    }

    return number == reversed_number;
}