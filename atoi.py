class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = 1
        st = ""
        n = False
        for c in s:
            if c in ["+", "-"] and not n and st == "":
                if c == "-":
                    sign *= -1
                n = True
            elif c in "0123456789" and c not in ["+", "-"]:
                if c == "0" and st != "":
                    st+= c
                elif c != "0":
                    st+=c
                n = True
            else:
                break
        rtr = 0  
        for m in st:
            rtr=rtr*10 + ord(m) - ord('0')
            if rtr * sign > 2147483647:
                return 2147483647
            elif rtr * sign <-2147483648:
                return -2147483648
        if not st:
            st = "0"
        
        return rtr * sign
        
