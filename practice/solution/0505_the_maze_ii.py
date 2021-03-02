import heapq

class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        
        value_dict = {(start[0], start[1]): 0}
        value_pq = []
        heapq.heappush(value_pq, (0, start[0], start[1]))
        res = -1
        
        while value_pq:
            cost, i, j = heapq.heappop(value_pq)
            
            if i == destination[0] and j == destination[1]:
                res = cost

                return res
            
            for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                count = 0
                row_end = i + a
                col_end = j + b
                
                while row_end >= 0 and row_end < len(maze) and col_end >= 0 and col_end < len(maze[0]) and maze[row_end][col_end] != 1:
                    row_end += a
                    col_end += b
                    count += 1

                row_end -= a
                col_end -= b
                temp_value = cost + count
                
                if not (row_end, col_end) in value_dict or value_dict[(row_end, col_end)] > temp_value:
                    value_dict[(row_end, col_end)] = temp_value
                    heapq.heappush(value_pq, (temp_value, row_end, col_end))
                                   
        return res