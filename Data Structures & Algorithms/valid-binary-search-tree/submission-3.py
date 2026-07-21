# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        order = []
        self.inOrder(root, order)

        for i in range(1, len(order)):
            if order[i] <= order[i - 1]:
                return False
        
        return True






    def inOrder(self, node, res):
        if node is None:
            return
        
        self.inOrder(node.left, res)
        res.append(node.val)
        self.inOrder(node.right, res)