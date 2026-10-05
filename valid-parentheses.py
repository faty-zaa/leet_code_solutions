class Solution:
    def isValid(self, s: str) -> bool:
        dct = {"(":")",
        "{":"}",
        "[":"]"
        }
        lst = []
        count1 = 0
        count2 = 0
        for i in s:
            if i in dct.keys():
                count1 += 1
            if i in dct.values():
                if lst and dct[lst.pop(-1)] != i:
                    return False
                count2 +=1 
            else:
                lst.append(i)      
        if lst or count1 != count2:
            return False
        else:
            return True


  
