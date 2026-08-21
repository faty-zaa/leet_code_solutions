from functools import reduce
from operator import mul
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output= [1] * n
        pr = 1
        for i in range(n):
            output[i] = pr
            pr *= nums[i]
        suf = 1
        for j in range(n-1, -1, -1):
            output[j] *= suf
            suf *= nums[j]
        return output

