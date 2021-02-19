class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        
        dp_list = [[0, 0]]
        self.res = 0
        
        for value in sorted(zip(startTime, endTime, profit), key=lambda x: x[1]):
            temp_value = self.helper(dp_list, value[0] + 1) - 1
            
            if dp_list[temp_value][1] + value[2] > dp_list[-1][1]:
                dp_list.append([value[1], dp_list[temp_value][1] + value[2]])
        
        self.res = dp_list[-1][1]
        
        return self.res
        
    def helper(self, value_list, target):
        low = 0
        high = len(value_list)
        
        while low < high:
            mid = (low + high) // 2
            
            if value_list[mid][0] < target:
                low = mid + 1
            else:
                high = mid
                
        return low