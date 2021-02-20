class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        value_dict = collections.Counter(nums)
        res = False
        
        for key in sorted(set(nums)):
            if value_dict[key] > 0:
                for i in reversed(range(k)):
                    value_dict[key + i] -= value_dict[key]
                    
                    if value_dict[key + i] < 0:
                        
                        return res
               
        res = True   
        
        return res