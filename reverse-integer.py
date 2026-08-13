
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < -2**31 or x > 2**31 - 1:
            return 0
        elif x < 0:
            sign *= -1
            x *= -1
        lst_num = list(str(x))
        lst_num.reverse()
        x = int("".join(lst_num))
        if x < -2**31 or x > 2**31 - 1:
            return 0
        return(sign * x)

        