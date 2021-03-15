class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        res = 1
        k -= 1
        
        while k > 0:
            temp_value = self.helper(res, res + 1, n)
            
            if temp_value <= k:
                res += 1
                k -= temp_value
            else:
                res *= 10
                k -= 1
                
        return res

    def helper(self, start, end, target):
        temp_value = 0
        
        while start <= target:
            temp_value += max(0, min(target + 1, end) - start)
            start *= 10
            end *= 10
            
        return temp_value