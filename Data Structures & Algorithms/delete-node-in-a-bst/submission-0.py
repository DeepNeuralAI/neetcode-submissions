# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.dfs(root, key)


    def dfs(self, node, key):
        if node is None:
            return
        
        if key < node.val:
            node.left = self.dfs(node.left, key)
        elif key > node.val:
            node.right = self.dfs(node.right, key)
        else:
            if node.left is None and node.right is None:
                return None
            
            if not node.left:
                return node.right
            
            if not node.right:
                return node.left
            
            predecessor = self.findPredecessor(node.left)
            node.val = predecessor.val
            node.left = self.dfs(node.left, predecessor.val)
        
        return node
    
    def findPredecessor(self, node):
        while node.right:
            node = node.right
        return node
        
