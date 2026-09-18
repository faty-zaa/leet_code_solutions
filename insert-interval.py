class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        new = []
        new.extend(newInterval)
        for i in intervals:
            if newInterval[0] in range(i[0], i[1]+1) or newInterval[1] in range(i[0], i[1]+1):
                new.extend(i)
        new_l= []
        new = sorted(new)
        final = []
        if new:
            new_l.extend([new[0], new[-1]])
        for lst in intervals:
            if not(lst[0] in range(new_l[0], new_l[1] + 1) or lst[1] in range(new_l[0], new_l[1] + 1)):
                final.append(lst)
        final.append(new_l)
        final.sort()
        return final




