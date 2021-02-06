class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        res = []
        
        for value in sorted(people, key=lambda x:(-x[0], x[1])):
            res.insert(value[1], value)
            
        return res