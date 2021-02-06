class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    
        sum_value = sum(nums)
        self.value_dict = set()
        self.res = False

        if sum_value % 2:
            
            return self.res

        self.res = self.dfs(nums, sum_value // 2)
   
        return self.res
    

    def dfs(self, nums, target):
        if target == 0:

            return True

        if target < 0 or target in self.value_dict:

            return False
        
        self.value_dict.add(target)

        for i in range(len(nums)):
            if self.dfs(nums[i + 1:], target - nums[i]): 
                return True

        return False