class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        value_list = sorted(nums)
        res = 0
        
        for i in reversed(range(1, len(value_list))):
            left = 0
            right = i - 1
                          
            while left < right:
                if value_list[right] + value_list[left] > value_list[i]:
                    res += right - left
                    right -= 1
                else:
                    left += 1
                    
        return res