class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        value_list = list(str(n))
        left = len(value_list) - 1
        right = len(value_list) - 1
        res = -1
        
        if len(value_list) == 1:
          
            return res
        
        while left > 0 and value_list[left - 1] >= value_list[left]:
            left -= 1
        
        if left == 0:
            
            return res

        while value_list[left - 1] >= value_list[right]:
            right -= 1
        
        # temp_value = value_list[right]
        # value_list[right] = value_list[left - 1]
        # value_list[left - 1] = temp_value
        value_list[left - 1], value_list[right] = value_list[right], value_list[left - 1]
        temp_value = int(''.join(value_list[:left] + value_list[left:][::-1]))

        if temp_value < 2 ** 31 and temp_value != n:
            res = temp_value
        
        return res