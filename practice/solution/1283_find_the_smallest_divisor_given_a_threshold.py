class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        low = 1
        high = max(nums)
        res = 0
        
        while low < high:
            mid = (low + high) // 2
            
            if self.helper(nums, mid) > threshold:
                low = mid + 1
            else:
                high = mid
                
        res = low
        
        return res
    
    def helper(self, nums, target):
        temp_value = 0
        
        if not target:
            
            return temp_value
        
        for num in nums:
            temp_value += (num + (target - 1)) / target
            
        return temp_value