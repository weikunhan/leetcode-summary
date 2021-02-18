class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        
        row_end = d
        col_end = target
        dp_list = [[0] * (col_end + 1) for _ in range(row_end + 1)]
        dp_list[0][0] = 1
        res = 0
        
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                for k in range(1, min(j, f) + 1):
                    dp_list[i][j] += dp_list[i - 1][j - k] % (10**9 + 7)
                    
        res = dp_list[-1][-1] % (10**9 + 7)

        return res