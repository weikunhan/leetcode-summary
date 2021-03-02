import random

class Solution(object):
    def __init__(self, w):
        """
        :type w: List[int]
        """
        
        self.value_list = w
        
        for i in range(1, len(w)):
            self.value_list[i] += self.value_list[i - 1]

    def pickIndex(self):
        """
        :rtype: int
        """
        
        temp_value = 0
        low = 0
        high = len(self.value_list)
        target_value = random.randint(1, self.value_list[-1])
        
        while low < high:
            mid = (low + high) // 2
            
            if self.value_list[mid] < target_value:
                low = mid + 1
            else:
                high = mid
        
        temp_value = low
                
        return temp_value
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()