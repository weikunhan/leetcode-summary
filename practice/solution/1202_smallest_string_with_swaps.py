import collections

class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        
        self.parent_value_list = range(len(s))
        value_dict = collections.defaultdict(list)
        self.res = '' 
        
        for a, b in pairs:
            self.union(a, b)
            
        for i in range(len(s)):
            value_dict[self.find(i)].append(s[i])
            
        for key, value in value_dict.items():
            value_dict[key] = sorted(value, reverse=True)
            
        for i in range(len(s)):
            self.res += value_dict[self.find(i)].pop()
            
        return self.res
  
    def find(self, x):
        if x != self.parent_value_list[x]:
            self.parent_value_list[x] = self.find(self.parent_value_list[x])
            
        return  self.parent_value_list[x]
        
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        self.parent_value_list[root_x] = root_y