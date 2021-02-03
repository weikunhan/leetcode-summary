class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
            
        low = 0
        high = len(nums) - 1
        res = 0
        
        while low < high:
            mid = (low + high) // 2
            
            if nums[mid] <= nums[mid + 1]:
                low = mid + 1
            else:
                high = mid
            
        res = low
        
        return res
