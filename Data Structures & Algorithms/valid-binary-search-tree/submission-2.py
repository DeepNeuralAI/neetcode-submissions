# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float('-inf'), float('inf'))


    def isValid(self, node, minValue, maxValue):
        if node is None:
            return True
        
        if not (minValue < node.val < maxValue):
            return False
        
        left = self.isValid(node.left, minValue, node.val)
        right = self.isValid(node.right, node.val, maxValue)

        return left and right

       