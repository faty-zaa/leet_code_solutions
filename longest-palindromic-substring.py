class Solution:
    def _is_palin(self, s: str):
        if s != s[::-1]:
            return False
        else:
            return True

    def longestPalindrome(self, s: str) -> str:
        lst = []
        ln = []
        l = len(s)

        if l == 1:
            return s
        for i in range(l):
            char = s[i]
            step = 1

            while i - step >= 0 and i + step < l:
                if s[i - step] != s[i + step]:
                    break

                char = s[i - step] + char + s[i + step]
                lst.append(char)
                ln.append(len(char))

                step += 1
        char = ""

        for j in range(l):
            if j + 1 < l:
                if s[j] == s[j + 1]:
                    char = s[j] + s[j + 1]
                    lst.append(char)
                    ln.append(len(char))

                    step = 1

                    while j - step >= 0 and j + 1 + step < l:
                        if s[j - step] != s[j + 1 + step]:
                            break

                        char = s[j - step] + char + s[j + 1 + step]
                        lst.append(char)
                        ln.append(len(char))

                        step += 1

        if ln:
            index = ln.index(max(ln))
            return lst[index]

        return s[0]