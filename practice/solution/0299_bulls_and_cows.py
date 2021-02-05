from collections import Counter

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
        bull_value = 0
        cow_value = 0
        value_dict = Counter()
        res = ''
       
        for a, b in zip(secret, guess):
            if a == b:
                bull_value += 1
            else:
                value_dict[a] += 1
                
        for a, b in zip(secret, guess):
            if a != b and value_dict[b]:
                cow_value += 1
                value_dict[b] -= 1
        
        res = str(bull_value) + "A" + str(cow_value) + "B"
        
        return res