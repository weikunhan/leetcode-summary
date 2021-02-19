class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        value_list = []
        self.res = 0
        
        for num in nums:
            temp_value = self.helper(value_list, num)
            
            if temp_value == len(value_list):
                value_list.append(num)
            else:
                value_list[temp_value] = num
                
        self.res = len(value_list)
        
        return self.res
    
    def helper(self, value_list, target):
        low = 0
        high = len(value_list)
        
        while low < high:
            mid = (low + high) // 2
            
            if value_list[mid] < target:
                low = mid + 1
            else:
                high = mid
                
        return low