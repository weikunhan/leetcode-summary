class TrieNode(object):
    def __init__(self):
        self.next = {}
        self.word = ''

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """

        self.value_trie = TrieNode()
        self.max_value = len(words[0])
        self.res = []
       
        for word in words:
            temp_root = self.value_trie
            
            for char in word:
                if not char in temp_root.next:
                    temp_root.next[char] = TrieNode()
                
                temp_root = temp_root.next[char]
                
            temp_root.word = word
            
        self.dfs([])
        
        return self.res

    def dfs(self, value_list):
        if len(value_list) == self.max_value:
            self.res.append(value_list)
            
            return        

        temp_value = ''
        temp_root = self.value_trie
        
        for word in value_list:
            temp_value += word[len(value_list)]

        for char in temp_value:
            if char not in temp_root.next:
                
                return
            
            temp_root = temp_root.next[char]
        
        temp_list = self.helper(temp_root)
        
        for word in temp_list:
            self.dfs(value_list + [word])
            
    def helper(self, root):
        temp_list = []
        
        if root.word:
            temp_list = [root.word]
            
            return temp_list
        
        for key, value in root.next.items():
            temp_list += self.helper(value)
            
        return temp_list