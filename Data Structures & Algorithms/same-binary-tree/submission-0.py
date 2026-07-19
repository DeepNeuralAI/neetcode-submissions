# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.solve(p, q)


    def solve(self, nodeA, nodeB):
        if nodeA is None and nodeB is None:
            return True

        if (nodeA is None and nodeB) or (nodeB is None and nodeA):
            return False
        
        if nodeA.val != nodeB.val:
            return False
        
        left = self.solve(nodeA.left, nodeB.left)
        right = self.solve(nodeA.right, nodeB.right)

        return left and right
        