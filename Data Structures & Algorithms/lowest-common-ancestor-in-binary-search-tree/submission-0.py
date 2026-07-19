# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.find(root, p, q)

    def find(self, node, p, q):
        if node is None:
            return

        if p.val < node.val and q.val < node.val:
            return self.find(node.left, p, q)
        elif p.val > node.val and q.val > node.val:
            return self.find(node.right, p, q)
        else:
            return node
        


        