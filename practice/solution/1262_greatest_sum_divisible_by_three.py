class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp_list = [0, 0, 0]
        res = 0
        
        for num in nums:
            value_list = [dp_list[0], dp_list[1], dp_list[2]]
            
            for value in value_list:
                dp_list[(num + value) % 3] = max(dp_list[(num + value) % 3], num + value)
                
        res = dp_list[0]
                
        return res