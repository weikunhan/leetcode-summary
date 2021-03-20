import collections

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        
        self.value_list = [-1] * n
        self.value_graph = collections.defaultdict(set)
        self.res = []
        
        for node, neighbor in connections:
            self.value_graph[node].add(neighbor)
            self.value_graph[neighbor].add(node)
        
        self.dfs(None, 0, 0)
        
        return self.res
    
    def dfs(self, root_p, root_c, count):
        self.value_list[root_c] = count + 1
        
        for neighbor in self.value_graph[root_c]:
            if root_p == neighbor:
                continue
            elif self.value_list[neighbor] == -1:
                temp_value = self.dfs(root_c, neighbor, count + 1)
                self.value_list[root_c] = min(temp_value, self.value_list[root_c])
            else:
                self.value_list[root_c] = min(self.value_list[root_c], self.value_list[neighbor])
                
        if self.value_list[root_c] == count + 1 and root_c:
            self.res.append([root_p, root_c])
            
        return self.value_list[root_c]
        