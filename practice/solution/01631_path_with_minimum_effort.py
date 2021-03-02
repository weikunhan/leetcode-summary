import heapq

class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """

        value_pq = []
        heapq.heappush(value_pq, (0, 0, 0))
        value_dict = {(0, 0): 0}
        res = 0
        
        while value_pq:
            cost, i, j = heapq.heappop(value_pq)

            if i == len(heights) - 1 and j == len(heights[0]) - 1:
                res = cost

                return res

            for a, b in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if a >= 0 and a < len(heights) and b >= 0 and b < len(heights[0]):
                    temp_value = max(cost, abs(heights[i][j] - heights[a][b]))
    
                    if not (a, b) in value_dict or value_dict[(a, b)] > temp_value:
                        heapq.heappush(value_pq, (temp_value, a, b))
                        value_dict[(a, b)] = temp_value
                        
        return res