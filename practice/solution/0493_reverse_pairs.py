class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        value_dict = {}
        pair_value_list = []
        value_list = []
        max_value = 0
        count = 1
        res = 0
        
        for num in nums:
            pair_value_list.append(num * 2)
            
        pair_value_list += nums
        max_value = len(set(pair_value_list)) + 1
        value_list = [0] * (max_value)
        
        for key in sorted(set(pair_value_list)):
            value_dict[key] = count
            count += 1

        for num in reversed(nums):
            sum_value = 0
            index_value = value_dict[num] - 1

            while index_value:
                sum_value += value_list[index_value]
                index_value -= (index_value & -index_value)
                
            res += sum_value
            index_value = value_dict[num * 2]
            
            while index_value < max_value:
                value_list[index_value] += 1
                index_value += (index_value & -index_value)
            
        return res