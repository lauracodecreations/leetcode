class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
    
        lo = 0
        hi = len(nums) - 1
        
        while lo <= hi:
            mid = (lo+hi) // 2
            
            if nums[mid] < target:  # ans is at the right side
                # remove left side 
                lo = mid+1
            elif nums[mid] > target: # ans is at the left side
                # remove half of the righ site 
                hi = mid-1
            else:
                return mid
        return - 1 
    