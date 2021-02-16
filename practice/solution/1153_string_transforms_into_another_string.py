class Solution(object):
    def canConvert(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        
        value_dict = {}
        res = False
        
        if str1 == str2:
            res = True
            
            return res

        for a, b in zip(str1, str2):
            if not a in value_dict:
                value_dict[a] = b
            else:
                if value_dict[a] != b:
                    
                    return res
        
        if len(set(value_dict.values())) < 26:
            res = True
        
        return res