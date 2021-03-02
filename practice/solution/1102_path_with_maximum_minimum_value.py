import heapq

class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        
        value_pq = []
        heapq.heappush(value_pq, (-A[0][0], 0, 0))
        A[0][0] = -1
        res = A[-1][-1]
        
        while value_pq:
            cost, i, j = heapq.heappop(value_pq)
            res = min(res, -cost)
            
            if i == len(A) - 1 and j == len(A[0]) - 1:

                return res
            
            for a, b in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if a >= 0 and a < len(A) and b >= 0 and b < len(A[0]) and A[a][b] != -1:
                    heapq.heappush(value_pq, (-A[a][b], a, b))
                    A[a][b] = -1
                    
        return res