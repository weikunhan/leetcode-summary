class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        value_stack = []
        res = 0
        
        for char in S:
            if char == '(':
                value_stack.append(res)
                res = 0
            else:
                temp_value = value_stack.pop()
                res += temp_value + max(res, 1)
                
        return res