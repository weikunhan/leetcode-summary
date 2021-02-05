import collections

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
    
        count = 0
        res = sys.maxsize
        dp_list = [[0] * len(grid[0]) for _ in range(len(grid))]
        visit_value_list = [[0] * len(grid[0]) for _ in range(len(grid))]
    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if self.helper(i, j, grid, visit_value_list, dp_list) != count:
                        res = -1
                        
                        return res
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j] and dp_list[i][j] == count:
                    res = min(res, visit_value_list[i][j])
                    
        if res == sys.maxsize:
            res = -1
            
        return res       
                    
    def helper(self, row, col, grid, visit_value_list, dp_list):
        value_list = collections.deque([(row, col, 0)])
        visit_dict = set([(row, col)])
        count = 1

        while value_list:
            i, j, cost = value_list.popleft()
            
            for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if a >= 0 and a < len(grid) and b >= 0 and b < len(grid[0]) and not (a, b) in visit_dict:
                    if not grid[a][b]:
                        value_list.append((a, b, cost + 1))
                        dp_list[a][b] += 1
                        visit_value_list[a][b] += cost + 1
                    
                    if grid[a][b] == 1:
                        count += 1
                        
                    visit_dict.add((a, b))
                        
        return count