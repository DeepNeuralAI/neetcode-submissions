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
    
        def dfs(node):
            if node is None:
                return (True, 0)
            
            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)
            
            current_height = 1 + max(left_height, right_height)

            if not (left_balanced and right_balanced):
                return (False, current_height)
            
            if abs(left_height - right_height) > 1:
                return (False, current_height)
            
            return (True, current_height)
        
        return dfs(root)[0]

        