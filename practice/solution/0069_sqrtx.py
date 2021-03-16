class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        temp_value = x
        res = 0
        
        while temp_value * temp_value > x:
            temp_value = (temp_value + x // temp_value) // 2
            
        res = temp_value
        
        return res
