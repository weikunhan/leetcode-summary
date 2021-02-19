class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """

        value_list = []
        self.res = []
        
        for word in words:
            value_list.append(word.count(min(word)))
        
        value_list = sorted(value_list)
        
        for query in queries:
            temp_value = self.helper(value_list, query.count(min(query)) + 1)
            self.res.append(len(value_list) - temp_value)
            
        return self.res   
        
    def helper(self, value_list, target):
        low = 0
        high = len(value_list)
        
        while low < high:
            mid = (low + high) // 2
            
            if value_list[mid] < target:
                low = mid + 1
            else:
                high = mid
                
        return low