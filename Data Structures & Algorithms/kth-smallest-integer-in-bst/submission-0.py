# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = k
        self.ans = None
        self.dfs(root)
        return self.ans
    


    def dfs(self, node):
        if node is None:
            return
        
        self.dfs(node.left)
        
        self.cnt -= 1

        if self.cnt == 0:
            self.ans = node.val
            return
        
        self.dfs(node.right)
        