# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, float('-inf'))
    
    def dfs(self, node, maxSeen):
        if node is None:
            return 0
        
        current_count = 0
        if node.val >= maxSeen:
            maxSeen = node.val
            current_count = 1
        
        current_count += self.dfs(node.left, maxSeen)
        current_count += self.dfs(node.right, maxSeen)
        
        return current_count