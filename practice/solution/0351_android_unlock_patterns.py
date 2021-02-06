class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        dp_list = [False] * 10
        self.value_dict = {(1, 3): 2, (1, 7): 4, (1, 9): 5, (2, 8): 5, (3, 7): 5, (3, 1): 2, (3, 9): 6, (4, 6): 5, (6, 4): 5, (7, 1): 4, (7, 3): 5, (7, 9): 8, (8, 2): 5, (9, 7): 8, (9, 3): 6, (9, 1): 5}
        self.res = 0
        
        self.dfs(m, n, [], dp_list)
            
        return self.res
    
    def dfs(self, start, end, value_list, dp_list):
        if len(value_list) >= start:
            self.res += 1
		
        if len(value_list) == end:
            
            return
        
        if value_list:
            dp_list[value_list[-1]] = True
        
        for i in range(1, 10):
            if not value_list:
                self.dfs(start, end, value_list + [i], dp_list)
            else:
                temp_value = value_list[-1]
            
                if not dp_list[i] and (not (temp_value, i) in self.value_dict or dp_list[self.value_dict[(temp_value, i)]]):
                    self.dfs(start, end, value_list + [i], dp_list)

        if value_list: 
            dp_list[value_list[-1]] = False