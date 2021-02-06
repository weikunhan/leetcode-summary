# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.total_value = 0
        self.res = 0
        
        self.total_value = self.postorder(root)
        self.postorder(root) 
        self.res %= (10**9 + 7)
        
        return self.res
    
    def postorder(self, root):
        temp_value = 0
        
        if not root:
            
            return temp_value
        
        left_value = self.postorder(root.left)
        right_value = self.postorder(root.right)
        self.res = max(self.res, max(left_value * (self.total_value - left_value), right_value * (self.total_value - right_value)))
        temp_value = left_value + right_value + root.val
        
        return temp_value