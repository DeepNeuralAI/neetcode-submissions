# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if not (p or q):
                return True
            
            if not (p and q):
                return False
            
            if p.val != q.val:
                return False
            
            leftSubtree = isSame(p.left, q.left)
            rightSubtree = isSame(p.right, q.right)

            return leftSubtree and rightSubtree
        

        if not subRoot:
            return True
        
        if not root:
            return False
        
        if isSame(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

            