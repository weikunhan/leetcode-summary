class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        self.res = []
        
        self.dfs(sorted(nums), [])
        
        return self.res
        
    def dfs(self, nums, value_list):
        if not nums:
            self.res.append(value_list)
            
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            self.dfs(nums[:i] + nums[i + 1:], value_list + [nums[i]])