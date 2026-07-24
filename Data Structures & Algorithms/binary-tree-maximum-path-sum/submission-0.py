# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSoFar = float('-inf')
        self.pathSum(root)
        return self.maxSoFar


    def pathSum(self, node):
        # Post-order traversal
        if node is None:
            return 0

        left_gain = max(0, self.pathSum(node.left))
        right_gain = max(0, self.pathSum(node.right))

        self.maxSoFar = max(
            node.val + left_gain + right_gain,
            self.maxSoFar
        )

        return node.val + max(left_gain, right_gain)


    

        

        