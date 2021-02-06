import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        
        value_pq = []
        value_dict = set()
        res = 0

        for i in range(len(heightMap)):
            for j in range(len(heightMap[0])):
                if not i or not j or i == len(heightMap) - 1 or j == len(heightMap[0]) - 1:
                    heapq.heappush(value_pq, (heightMap[i][j], i, j))
                    value_dict.add((i, j))
 
        while value_pq:
            cost, i, j = heapq.heappop(value_pq)    
            
            for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if a >= 0 and a < len(heightMap) and b >= 0 and b < len(heightMap[0]) and not (a, b) in value_dict:
                    res += max(0, cost - heightMap[a][b])
                    heapq.heappush(value_pq, (max(cost, heightMap[a][b]), a, b))
                    value_dict.add((a, b))
                    
        return res