import collections

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        
        value_dict = {}
        res =  False
        
        for i in range(len(graph)):
            if not i in value_dict and graph[i]:
                value_dict[i] = 1
                value_list = collections.deque([i])
                
                while value_list:
                    temp_value = len(value_list)
                    
                    for _ in range(temp_value):
                        temp_node = value_list.popleft()
                        
                        for neighbor in graph[temp_node]:
                            if not neighbor in value_dict:
                                value_dict[neighbor] = -value_dict[temp_node]
                                value_list.append(neighbor)
                            
                            if value_dict[neighbor] == value_dict[temp_node]:
                                
                                return res
                            
        res = True
        
        return res