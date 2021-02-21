class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        value_list = path.split('/')
        value_stack = []
        res = '/'
        
        for path in value_list:
            if path and path != '.':
                if path != '..':
                    value_stack.append(path)
                else:
                    if value_stack:
                        value_stack.pop()               
                    
        res += '/'.join(value_stack)
        
        return res
                    
