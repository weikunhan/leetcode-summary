class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        
        self.value_list = []
        self.res = 0

        for envelope in sorted(envelopes, key=lambda x:(x[0], -x[1])):
            temp_value = self.helper(envelope[1])
                
            if temp_value == len(self.value_list):
                self.value_list.append(envelope[1])
            else:
                self.value_list[temp_value] = envelope[1]

        self.res = len(self.value_list)      
                
        return self.res
    
    def helper(self, target):
        low = 0
        high = len(self.value_list)
        
        while low < high:
            mid = (low + high) // 2
            
            if self.value_list[mid] < target:
                low = mid + 1
            else:
                high = mid
                
        return low