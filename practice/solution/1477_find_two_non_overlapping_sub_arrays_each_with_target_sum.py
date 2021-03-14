class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        
        value_dict = {0: -1}
        value_list = [sys.maxsize] * len(arr)
        presum_value = 0
        temp_value = sys.maxsize
        res = sys.maxsize
        
        for i in range(len(arr)):
            presum_value += arr[i]
            
            if presum_value - target in value_dict:
                index_value = value_dict[presum_value - target]
                
                if index_value != -1:
                    res = min(res, i - index_value + value_list[index_value])
                    
                temp_value = min(temp_value, i - index_value)
            
            value_list[i] = temp_value
            value_dict[presum_value] = i
        
        if res == sys.maxsize:
            res = -1
                
        return res