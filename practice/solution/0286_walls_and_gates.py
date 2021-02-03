import collections

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        
        value_list = collections.deque()
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if not rooms[i][j]:
                    value_list.append((i, j))

        while value_list:
            temp_value = len(value_list)
            
            for _ in range(temp_value):
                i, j = value_list.popleft()
                
                for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if a >= 0 and a < len(rooms) and b >= 0 and b < len(rooms[0]) and rooms[a][b] > 2**30:
                        rooms[a][b] = rooms[i][j] + 1
                        value_list.append((a, b))