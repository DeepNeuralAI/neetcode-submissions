# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        isBalanced, height = self.height(root)

        return isBalanced
        
       
    def height(self, node):
        if node is None:
            return [True, 0]
        
        isBalanced = True
        
        left = self.height(node.left)
        right = self.height(node.right)

        if not left[0] or not right[0]:
            isBalanced = False

        if abs(left[1] - right[1]) > 1:
            isBalanced = False

        return [isBalanced, 1 + max(left[1], right[1])]
