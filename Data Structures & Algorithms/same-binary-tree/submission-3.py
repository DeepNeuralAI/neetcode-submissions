# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def is_same(p, q):
            if not (p or q):
                return True
            
            if not (p and q):
                return False
            
            if p.val != q.val:
                return False
            
            # Nodes have same value - check for subtrees
            return is_same(p.left, q.left) and is_same(p.right, q.right)
        
        return is_same(p, q)

        