class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        self.res = []
        
        self.dfs(0, 0, s, ['(', ')'])
        
        return self.res
    
    def dfs(self, start, end, s, value_list):
        count = 0
        
        for i in range(start, len(s)):
            if s[i] == value_list[0]:
                count += 1
            
            if s[i] == value_list[1]:
                count -= 1
                
            if count >= 0:
                continue
                
            for j in range(end, i + 1):
                if s[j] == value_list[1] and (j == end or s[j] != s[j - 1]):
                    self.dfs(i, j, s[:j] + s[j + 1:], value_list)
                    
            return
        
        s = s[::-1]

        if value_list[0] == '(':
            self.dfs(0, 0, s, [')', '('])
        else:
            self.res.append(s)