# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def height(node):
            if node is None:
                return 0
            
            left_h = height(node.left)
            right_h = height(node.right)
            return 1 + max(left_h, right_h)
    
        left_h = height(root.left)
        right_h = height(root.right)

        if abs(left_h - right_h) > 1:
            return False
        
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        
        return False