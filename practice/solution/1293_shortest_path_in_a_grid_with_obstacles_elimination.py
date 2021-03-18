import collections

class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        value_list = collections.deque([(0, 0, 0, 0)])
        value_dict = set()
        res = -1
        
        while value_list:
            temp_value = len(value_list)
            
            for _ in range(temp_value):
                i, j, state, cost = value_list.popleft()
                
                if state > k: 
                    continue
                
                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    res = cost
                    
                    return res
                
                for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if a >= 0 and a < len(grid) and b >= 0 and b < len(grid[0]):
                        if grid[a][b]:
                            next_state = state + 1
                        else:
                            next_state = state
    
                        if not (a, b, next_state) in value_dict:
                            value_dict.add((a, b, next_state))
                            value_list.append((a, b, next_state, cost + 1))
        
        return res