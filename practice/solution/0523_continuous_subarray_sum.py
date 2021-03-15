class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        value_dict = {0: -1}
        presum_value = 0
        res = False
        
        if not k:
            for i in range(len(nums) - 1):
                if nums[i] == nums [i + 1] == 0:
                    res = True
            
            return res
        
        for i in range(len(nums)):
            presum_value += nums[i]

            if presum_value % k in value_dict:
                index_value = value_dict[presum_value % k]
                
                if i - index_value > 1:
                    res = True
                
                    return res
            else:
                value_dict[presum_value % k] = i
        
        return res