class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        self.res = False
        self.temp_value = 0.001
        value_list = []
        
        for num in nums:
            value_list.append(float(num))
        
        self.res = self.dfs(value_list)
        
        return self.res
    
    def dfs(self, value_list):
        if len(value_list) == 1: 
            if abs(value_list[0] - 24) <= self.temp_value:
                
                return True
            
        for i in range(len(value_list)):
            for j in range(i):
                a = value_list.pop(i)
                b = value_list.pop(j)
                temp_list = [a + b, a - b, b - a, a * b]
                
                if a > self.temp_value: 
                    temp_list.append(b / a)
                    
                if b > self.temp_value: 
                    temp_list.append(a / b)
                    
                for num in temp_list:
                    if self.dfs(value_list + [num]): 
                        
                        return True

                value_list.insert(j, b)
                value_list.insert(i, a)
                
        return False