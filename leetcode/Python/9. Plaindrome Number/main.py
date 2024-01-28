class Solution:
    def isPalindrome(self, number: int) -> bool:
        if number < 0:
            return False
        if number == 0:
            return True

        tmp = number
        reversed_number = 0

        while tmp > 0:
            digit = tmp % 10
            tmp //= 10
            reversed_number = reversed_number * 10 + digit

        return number == reversed_number
