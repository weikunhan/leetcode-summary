class Solution(object):
    def numberOfArrays(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        row_end = len(s)
        dp_list = [0] * (row_end + 1)
        dp_list[0] = 1
        dp_list[1] = 1
        res = 0
        
        for i in range(1, len(s)):
            for j in range(len(str(k))):
                if i - j >= 0 and 1 <= int(s[i - j:i + 1]) <= k and s[i - j:i + 1][0] != '0':
                    dp_list[i+1] += dp_list[i - j]
        
        res = dp_list[-1] % (10**9 + 7)
        
        return res