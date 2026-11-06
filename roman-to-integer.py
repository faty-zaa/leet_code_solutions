class Solution:
    def romanToInt(self, s: str) -> int:
        a = 0
        i = 0
        l = len(s)
        hach= {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        while i < l:
            if s[i] == 'I' and i+1 < l and s[i+1] in ['V', 'X']:
                a += (hach[s[i+1]] - hach[s[i]])
                i+=1
            elif s[i] == 'X' and i+1 < l and s[i+1] in ['L', 'C']:
                a += (hach[s[i+1]] - hach[s[i]])
                i+=1
            elif s[i] == 'C' and i+1 < l and s[i+1] in ['D', 'M']:
                a += (hach[s[i+1]] - hach[s[i]])
                i+=1
            else:
                a+= hach[s[i]]
            i+=1
        return a


        
