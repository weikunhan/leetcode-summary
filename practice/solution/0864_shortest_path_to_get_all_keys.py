import collections

class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        
        final_value = 0
        value_list = collections.deque()
        value_dict = set()
        res = -1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in "abcdef":
                    final_value |= 1 << ord(grid[i][j]) - ord("a")
                
                if grid[i][j] == "@":
                    value_list.append((i, j, 0, 0))
                    
        while value_list:
            temp_value = len(value_list)
            
            for _ in range(temp_value):
                i, j, state, cost = value_list.popleft()

                if state == final_value: 
                    res = cost

                    return res

                for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if a >= 0 and a < len(grid) and b >= 0 and b < len(grid[0]) and grid[a][b] != '#':
                        if grid[a][b].isupper() and not state & 1 << (ord(grid[a][b].lower()) - ord("a")): 
                            continue

                        if ord(grid[a][b]) >= ord("a"):
                            next_state = state | 1 << (ord(grid[a][b]) - ord("a")) 
                        else:
                            next_state = state

                        if not (a, b, next_state) in value_dict:
                            value_dict.add((a, b, next_state))
                            value_list.append((a, b, next_state, cost + 1))
        
        return res