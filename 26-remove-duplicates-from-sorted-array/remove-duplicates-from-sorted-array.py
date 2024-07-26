class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L=0
        lastseen=None
        for R in range(len(nums)): 
            if nums[R] != lastseen:
                lastseen=nums[R]
                nums[R], nums[L] = nums[L], nums[R]
                L+=1
        
        return L

                