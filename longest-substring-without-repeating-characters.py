class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dct = {}
        sl = list(s)
        lst = []
        char = []
        for i in range(len(s)):
            if s[i] not in char:
                char.append(s[i])
            else:
                lst.append(len(char))
                f = dct[s[i]]
                char = list(s[f + 1:i + 1])
            dct[s[i]] = i
        lst.append(len(char))     
        return(max(lst))

            