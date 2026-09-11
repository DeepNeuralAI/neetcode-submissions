# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.res = root.val

        def dfs(node):
            # Returns the max path of the node
            if node is None:
                return 0
            
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            current_max = node.val + left + right
            self.res = max(self.res, current_max)
            return node.val + max(left, right)
        
        dfs(root)
        return self.res