from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        uni = set(nums)
        maxi = sorted(count.values(), reverse=True)
        lst = []
        n = 0
        for num in uni:
            if count[num] in maxi[:k]:
                lst.append(num)

        return lst

