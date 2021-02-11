class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        value_stack = []
        data_value_dict = {}
        visit_value_dict = set()
        res = ''
        
        for i in range(len(s)):
            data_value_dict[s[i]] = i 
        
        for i in range(len(s)):
            if not s[i] in visit_value_dict:
                while value_stack and value_stack[-1] > s[i] and data_value_dict[value_stack[-1]] > i:
                    temp_value = value_stack.pop()
                    visit_value_dict.remove(temp_value)
                    
                value_stack.append(s[i])
                visit_value_dict.add(s[i])
                
        res = ''.join(value_stack)
        
        return res