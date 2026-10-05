class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        ln = len(nums) - 1
        index = 0
        while l <= ln:
            index = l + (ln - l) // 2
            if nums[index] == target:
                return index
            elif nums[index] < target:
                l = index + 1

            else:
                ln = index - 1
        
        return -1
    
