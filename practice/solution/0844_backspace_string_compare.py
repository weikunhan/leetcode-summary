class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        a_value_stack = []
        b_value_stack = []
        res = False
        
        for char in S:
            if char != '#':
                a_value_stack.append(char)
            else:
                if a_value_stack:
                    a_value_stack.pop()

        for char in T:
            if char != '#':
                b_value_stack.append(char)
            else:
                if b_value_stack:
                    b_value_stack.pop()

        if a_value_stack == b_value_stack:
            res = True
            
        return res