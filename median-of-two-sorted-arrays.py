class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums = sorted(nums1)
        l = len(nums)
        if ((l % 2) != 0):
            return nums[l//2]
        else:
            ln = l// 2
            summ = (nums[ln -1] + nums[ln]) / 2
            return summ