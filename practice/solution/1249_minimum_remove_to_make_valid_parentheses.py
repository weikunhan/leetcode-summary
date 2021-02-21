class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        value_stack = []
        value_list = list(s)
        res = ''
        
        for i in range(len(s)):
            if s[i] == '(':
                value_stack.append(i)
            
            if s[i] == ')':
                if value_stack:
                    value_stack.pop()
                else:
                    value_list[i] = '#'
        
        while value_stack:
            temp_value = value_stack.pop()
            value_list[temp_value] = '#'
            
        for value in value_list:
            if not value == '#':
                res += value
        
        return res