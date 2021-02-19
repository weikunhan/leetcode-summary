class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        
        value_list = []
        self.res = 0

        for envelope in sorted(envelopes, key=lambda x:(x[0], -x[1])):
            temp_value = self.helper(value_list, envelope[1])
                
            if temp_value == len(value_list):
                value_list.append(envelope[1])
            else:
                value_list[temp_value] = envelope[1]

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