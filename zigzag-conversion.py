class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lentgh = len(s)
        if lentgh <= numRows or numRows == 1:
            return s
        strzig = []
        i = 0
        zig = 0

        zag = numRows - 2
        while i < lentgh:
            if zig % 2 == 0:
                char = s[i:i+numRows]
                strzig.append(list(char))
                i = i + numRows
            else:
                char = s[i:i+zag]
                strzig.append(list(char))
                i = i + zag
            zig += 1
        zig = 0
        row = 0
        strzag = ["" for _ in range(numRows)]
        for i in range(len(strzig)):
            for j in range(len(strzig[i])):
                if i % 2 == 0:
                    row = j
                else:
                    row = numRows - 2 - j
                strzag[row]+= strzig[i][j]
        return "".join(strzag)
               
