class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        
        self.res = []
        
        self.dfs(num, target, 0, None, [])
        
        return self.res
        
    def dfs(self, num, target, sum_value, temp_value, value_list):            
        if not num and sum_value == target:
            self.res.append(''.join(value_list))

        for i in range(1, len(num) + 1):
            num_value = int(num[:i])
            
            if i == 1 or (i > 1 and num[0] != '0'):
                if temp_value == None:
                    self.dfs(num[i:], target, num_value, num_value, value_list + [num[:i]])
                else:
                    self.dfs(num[i:], target, sum_value + num_value, num_value, value_list + ['+'] + [num[:i]])
                    self.dfs(num[i:], target, sum_value - num_value, -num_value, value_list + ['-'] + [num[:i]])
                    self.dfs(num[i:], target, sum_value - temp_value + temp_value * num_value, temp_value * num_value, value_list + ['*'] + [num[:i]])