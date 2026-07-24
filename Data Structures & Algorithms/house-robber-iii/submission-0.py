# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.solve(root))
    
    def solve(self, node):
        if not node:
            return [0, 0]
        
        l_rob, l_skip = self.solve(node.left)
        r_rob, r_skip = self.solve(node.right)

        take = node.val + l_skip + r_skip
        skip = max(l_rob, l_skip) + max(r_rob, r_skip)

        return [take, skip]
        



        