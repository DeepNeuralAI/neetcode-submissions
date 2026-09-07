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
                return (True, 0)
            
            left_bal, left_h = height(node.left)
            right_bal, right_h = height(node.right)
            current_height = 1 + max(left_h, right_h)

            if not (left_bal and right_bal):
                return (False, current_height)
            
            if abs(left_h - right_h) > 1:
                return (False, current_height)
            
            return (True, current_height)
        
        return height(root)[0]