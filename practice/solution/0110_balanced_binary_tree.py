# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        self.res = False

        if self.postorder(root) != -1:
            self.res = True
            
        return self.res
            
    def postorder(self, root):
        temp_value = 0
        
        if not root:
            
            return temp_value
        
        left_value  = self.postorder(root.left)
        right_value = self.postorder(root.right)
            
        if left_value == -1 or right_value == -1 or abs(left_value - right_value) > 1:
            temp_value = -1  
            
            return temp_value
        
        temp_value = 1 + max(left_value, right_value)
        
        return temp_value