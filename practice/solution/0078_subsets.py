class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        self.res = []
        
        self.dfs(nums, [])
        
        return self.res
    
    def dfs(self, nums, value_list):
        self.res.append(value_list)
        
        for i in range(len(nums)):
            self.dfs(nums[i + 1:], value_list + [nums[i]])