# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.res = 0
        
        self.res = self.dfs(root)
        
        return self.res
    
    def dfs(self, root):
        temp_value = 0
        
        if not root:
            
            return temp_value
        
        left_value = self.helper(root.left)
        right_value = self.helper(root.right)
            
        if left_value == right_value:
            temp_value = 2 ** left_value + self.dfs(root.right)

            return temp_value
        else:
            temp_value = 2 ** right_value + self.dfs(root.left)
            
            return temp_value 
        
    def helper(self, root):
        temp_value = 0
        
        if not root:
            
            return temp_value
        
        left_value = self.helper(root.left)
        tamp_value= 1 + left_value
        
        return tamp_value