import collections

class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        self.value_graph = collections.defaultdict(set)
        self.value_list = [1] * N
        self.res = [0] * N
        
        for node, neighbor in edges:
            self.value_graph[node].add(neighbor)
            self.value_graph[neighbor].add(node)
            
        self.postorder_dfs(None, 0, N)
        self.preorder_dfs(None, 0, N)
        
        return self.res
    
    def postorder_dfs(self, root_p, root_c, N):
        for neighbor in self.value_graph[root_c]:
            if neighbor != root_p:
                self.postorder_dfs(root_c, neighbor, N)
                self.value_list[root_c] += self.value_list[neighbor]
                self.res[root_c] += self.res[neighbor] + self.value_list[neighbor]
    
        
    def preorder_dfs(self, root_p, root_c, N):
        for neighbor in self.value_graph[root_c]:
            if neighbor != root_p:
                self.res[neighbor] = self.res[root_c] - self.value_list[neighbor] + N - self.value_list[neighbor]
                self.preorder_dfs(root_c, neighbor, N)