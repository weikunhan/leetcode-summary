class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    
        sum_value = sum(nums)
        dp_list = [False] * (sum_value // 2 + 1)
        self.res = False

        if sum_value % 2:
            
            return self.res

        self.res = self.dfs(0, nums, sum_value // 2, dp_list)
   
        return self.res
    

    def dfs(self, start, nums, target, dp_list):
        if not target:

            return True

        if target < 0 or dp_list[target]:

            return False
        
        dp_list[target] = True

        for i in range(start, len(nums)):
            if self.dfs(i + 1, nums, target - nums[i], dp_list): 
                
                return True

        return False