class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        self.res = 0
        
        self.res = self.dfs(s, k)
        
        return self.res
    
    def dfs(self, s, target):
        temp_value = 0
        count = 0

        if not s or len(s) < target:
            
            return temp_value
        
        while count < len(s) and s.count(s[count]) >= target:
            count += 1
            
        if count == len(s):
            temp_value = count
            
            return temp_value
        
        temp_value = max(temp_value, self.dfs(s[:count], target))
        temp_value = max(temp_value, self.dfs(s[count + 1:], target))
        
        return temp_value