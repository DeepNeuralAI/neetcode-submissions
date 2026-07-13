# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.solve(root)
        return root
    

    def solve(self, node):
        if node is None:
            return
        
        left = node.left
        right = node.right
        
        node.left = right
        node.right = left
        
        self.solve(node.left)
        self.solve(node.right)

        return node

