class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        row_end = len(text1)
        col_end = len(text2)
        dp_list = [[0] * (col_end + 1) for _ in range(row_end + 1)]
        res = 0
        
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp_list[i + 1][j + 1] = 1 + dp_list[i][j]
                else:
                    dp_list[i + 1][j + 1] = max(dp_list[i + 1][j], dp_list[i][j + 1])
                
        res = dp_list[-1][-1]
        
        return res