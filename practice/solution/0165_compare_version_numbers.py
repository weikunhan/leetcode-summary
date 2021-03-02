class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        a_value_list = [int(x) for x in version1.split(".")]
        b_value_list = [int(x) for x in version2.split(".")]
        res = 0
        
        for i in range(max(len(a_value_list),len(b_value_list))):
            if i < len(a_value_list):
                a_value = a_value_list[i]
            else:
                a_value = 0
                
            if i < len(b_value_list):
                b_value = b_value_list[i]
            else:
                b_value = 0
                
            if a_value > b_value:
                res = 1
                
                return res
            elif a_value < b_value:
                res = -1
                
                return res
            else:
                pass
        
        return res