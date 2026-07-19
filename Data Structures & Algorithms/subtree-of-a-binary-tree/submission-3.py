# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.isSame(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
       
        



    def isSame(self, nodeA, nodeB):
        if nodeA is None and nodeB is None:
            return True
        
        if (not nodeA or not nodeB) or (nodeA.val != nodeB.val):
            return False
        
        return (self.isSame(nodeA.left, nodeB.left) and
                self.isSame(nodeA.right, nodeB.right))
        