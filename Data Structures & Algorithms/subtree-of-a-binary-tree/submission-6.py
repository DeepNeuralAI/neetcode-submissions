# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if not (root and subRoot):
            return False

        def isSame(p, q):
            if not p and not q:
                return True
            
            if not (p and q):
                return False
            
            if p.val != q.val:
                return False
            
            left = isSame(p.left, q.left)
            right = isSame(p.right, q.right)

            return left and right
        
        if isSame(root, subRoot):
            return True

        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right
        
        
        
        
        

        


       