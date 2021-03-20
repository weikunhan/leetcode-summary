# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        
        self.res = []
        self.value_graph = collections.defaultdict(set)
        value_list = collections.deque([(target.val, 0)])
        value_dict = set([target.val])
        
        self.helper(None, root)
        
        while value_list:
            temp_value = len(value_list)

            if value_list[0][1] == K:
                for temp_node in value_list:
                    self.res.append(temp_node[0])
                    
                return self.res
            
            for _ in range(temp_value):
                temp_node, cost = value_list.popleft()
                
                for neighbor in self.value_graph[temp_node]:
                    if not neighbor in value_dict:
                        value_list.append((neighbor, cost + 1))
                        value_dict.add(neighbor)
        
        return self.res
        
    def helper(self, root_p, root_c):
        if not root_c:
            
            return 
        
        if root_p and root_c:
            self.value_graph[root_c.val].add(root_p.val)
            self.value_graph[root_p.val].add(root_c.val)
            
        self.helper(root_c, root_c.left)
        self.helper(root_c, root_c.right)
