class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        
        value_dict = {}
        res = []
        
        for i in range(len(words)):
            value_dict[words[i]] = i
            
        for key, value in value_dict.items():
            for i in range(len(key) + 1):
                prefix_value = key[:i]
                suffix_value = key[i:]
                
                if prefix_value == prefix_value[::-1]:
                    temp_value = suffix_value[::-1]
                    
                    if temp_value != key and temp_value in value_dict:
                        res.append([value_dict[temp_value],  value])
                        
                if i != len(key) and suffix_value == suffix_value[::-1]:
                    temp_value = prefix_value[::-1]
                    
                    if temp_value != key and temp_value in value_dict:
                        res.append([value, value_dict[temp_value]])
                        
        return res