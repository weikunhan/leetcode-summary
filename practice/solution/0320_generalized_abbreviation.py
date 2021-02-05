class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """

        self.res = []

        self.dfs(word, [])
        
        return self.res
        
    def dfs(self, word, value_list):
        if not word:
            self.res.append(''.join(value_list))
            
            return 
        
        for i in range(len(word) + 1):
            if not i:
                self.dfs(word[i + 1:], value_list + [word[i:i + 1]])
            else:
                self.dfs(word[i + 1:], value_list + [str(i)] + [word[i:i + 1]])
