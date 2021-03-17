import collections

class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.value_dict = collections.defaultdict(list)
        
    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        
        for word in dictionary:
            self.value_dict[len(word)].append(word)

    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        
        for word in self.value_dict[len(searchWord)]:
            count = 0
            
            for i in range(len(searchWord)):
                if word[i] != searchWord[i]:
                    count += 1
                    
            if count == 1:
                
                return True
            
        return False
        
        
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)