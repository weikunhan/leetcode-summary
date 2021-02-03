class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        value_dict = set()
        temp_value = n
        res = False
        
        while not temp_value in value_dict: 
            sum_value = 0
            
            for char in str(temp_value):
                sum_value += int(char) ** 2
            
            value_dict.add(temp_value)
            temp_value = sum_value

        if temp_value == 1:
            res = True
            
        return res