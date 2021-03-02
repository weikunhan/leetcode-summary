class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        temp_value = -sys.maxsize - 1
        res = 0
        
        for interval in sorted(intervals, key=lambda x:x[1]):
            if interval[0] >= temp_value:
                temp_value = interval[1]
            else:
                res += 1
                
        return res