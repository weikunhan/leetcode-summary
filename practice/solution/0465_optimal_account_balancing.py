import collections

class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        
        value_dict = collections.Counter()
        dp_list = []
        self.res = sys.maxsize
        
        for transaction in transactions:
            value_dict[transaction[0]] -= transaction[2]
            value_dict[transaction[1]] += transaction[2]
 
        for key, value in value_dict.items():
            if value:
                dp_list.append(value)
        
        self.dfs(0, 0, dp_list)

        return self.res

    def dfs(self, start, end, dp_list):
        while start < len(dp_list) and not dp_list[start]:
            start += 1
            
        if start == len(dp_list):
            self.res = min(self.res, end)
            
            return
        
        for i in range(start + 1, len(dp_list)):
            if (dp_list[i] < 0 and dp_list[start] > 0) or (dp_list[i] > 0 and dp_list[start] < 0):
                dp_list[i] += dp_list[start]
                self.dfs(start + 1, end + 1, dp_list)
                dp_list[i] -= dp_list[start]