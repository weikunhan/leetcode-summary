import heapq
import collections

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
        value_dict = collections.Counter(arr)
        value_pq = []
        res = 0
        
        for key, value in value_dict.items():
            heapq.heappush(value_pq, (value, key))
        
        while k > 0:
            k -= heapq.heappop(value_pq)[0]
        
        if k < 0:
            res = len(value_pq) + 1
        else:
            res = len(value_pq)

        return res