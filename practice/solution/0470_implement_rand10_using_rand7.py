# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        
        res = sys.maxsize
        
        while res >= 40:
            res = (rand7() - 1) * 7 + rand7() - 1
            
        res = res % 10 + 1
        
        return res