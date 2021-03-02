class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        self.res = 0
        
        self.res, _ = self.dfs(0, s + '+')
        
        return self.res
        
    def dfs(self, start, s):
        sum_value = 0
        value_stack = []
        sign = '+'
        
        while start < len(s):
            if s[start].isdigit():
                sum_value = 10 * sum_value + int(s[start])
            
            if s[start] in '+-*/()':
                if s[start] == '(':
                    sum_value, start = self.dfs(start+1, s)
                    continue
                
                if sign == '+':
                    value_stack.append(sum_value)
                    sign = s[start]
                elif sign == '-':
                    value_stack.append(-sum_value)
                    sign = s[start]
                elif sign == '*':
                    temp_value = value_stack.pop()
                    value_stack.append(temp_value * sum_value)  
                    sign = s[start]
                else:
                    temp_value = value_stack.pop()
                    #carry, remainder = divmod(temp_value, sum_value)
                    #if carry < 0 and remainder:
                    #    carry += 1
                    #value_stack.append(carry)
                    value_stack.append(int(temp_value / float(sum_value)))
                    sign = s[start]
                
                sum_value = 0
  
                if s[start] == ')':
                    temp_list = [sum(value_stack), start + 1]
                    
                    return temp_list
                      
            start += 1
           
        temp_list = [sum(value_stack), start]
                
        return temp_list