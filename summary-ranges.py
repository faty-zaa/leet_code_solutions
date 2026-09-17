class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        lst = []
        st = []
        if len(nums) == 0:
            return lst
        for n in range(len(nums)):
            if n - 1 >= 0 and nums[n - 1] + 1 != nums[n]:
                lst.append(st)
                st = []
            st.append(nums[n])
        lst.append(st)
        new = []
        for ls in lst:
            st = ""
            if len(ls) == 1:
                new.append(str(ls[0]))
            else:
                st += (str(ls[0]) + "->" + str(ls[-1]))
                new.append(st)


        return new
            

            
        
