# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = root.val
        cnt = 0
        # In order traversal will be sorted order
        
        def dfs(node):
            nonlocal cnt, res

            if node is None: 
                return 0
            
            dfs(node.left)
            cnt += 1
            
            if cnt == k:
                res = node.val
                return cnt
            
            dfs(node.right)
            
            return cnt
        
        dfs(root)
        return res