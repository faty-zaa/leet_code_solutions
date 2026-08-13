class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x <= -(2**31) or x >= 2**31 - 1:
            return False
        str_num = list(str(x))
        test = str_num[::-1]
        x1 = int("".join(test))
        if x1 <= -(2**31) or x1 >= 2**31 - 1:
            return False
        if x != x1:
            return False
        return True

