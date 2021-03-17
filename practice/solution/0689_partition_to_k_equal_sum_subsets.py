class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        sum_value = sum(nums)
        dp_list = [False] * len(nums)
        self.temp_value = sum_value // k
        self.res = False

        if sum_value % k:
            
            return self.res

        self.res = self.dfs(0, k, nums, sum_value // k, dp_list)
   
        return self.res
    

    def dfs(self, start, end, nums, target, dp_list):
        if end == 1:
            
            return True
        
        if not target and self.dfs(0, end - 1, nums, self.temp_value, dp_list):
                
            return True

        if target < 0:

            return False

        for i in range(start, len(nums)):
            if not dp_list[i]:
                dp_list[i] = True
                
                if self.dfs(i + 1, end, nums, target - nums[i], dp_list): 
                    
                    return True
                
                dp_list[i] = False

        return False