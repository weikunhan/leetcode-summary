class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        row_end = len(p)
        col_end = len(s)
        dp_list = [[False] * (col_end + 1) for _ in range(row_end + 1)]
        dp_list[0][0] = True
        res = False
        
        for i in range(len(p)):
            if p[i] != '*':
                break
                
            dp_list[i + 1][0] = True
                
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] != '*':
                    if dp_list[i][j] and (p[i] ==s[j] or p[i] == '?'):
                        dp_list[i + 1][j + 1] = True
                else:
                    if dp_list[i][j + 1]:
                        dp_list[i + 1][j + 1] = True
                        
                    if dp_list[i][j]:
                        dp_list[i + 1][j + 1] = True
                        
                    if dp_list[i + 1][j]:
                        dp_list[i + 1][j + 1] = True

        res = dp_list[-1][-1] 
            
        return res