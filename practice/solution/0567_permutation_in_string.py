class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        target_value_dict = collections.Counter(s1)
        count_value_dict = collections.Counter(s2[:len(s1) - 1])
        res = False
        
        for i in range(len(s1) - 1, len(s2)):
            count_value_dict[s2[i]] += 1
            index_value = i - len(s1) + 1
            
            if count_value_dict & target_value_dict == target_value_dict:
                res = True
                
                return res
                
            count_value_dict[s2[index_value]] -= 1
  
        return res