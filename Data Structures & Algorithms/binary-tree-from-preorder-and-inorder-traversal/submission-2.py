# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i
        
        self.preorder = preorder
        self.inorder = inorder
        self.inorder_map = inorder_map
        
        root = self.splitTree(0, len(preorder) - 1, 0, len(inorder) - 1)

        return root
    
    def splitTree(self, preStart, preEnd, inStart, inEnd):
        if preStart > preEnd or inStart > inEnd:
            return
        
        root_val = self.preorder[preStart]
        mid = self.inorder_map[root_val]
        left_subtree_size = mid - inStart
        
        root = TreeNode(root_val)

        root.left = self.splitTree(preStart + 1, preStart + left_subtree_size, inStart, mid - 1)
        root.right = self.splitTree(preStart + left_subtree_size + 1, preEnd, mid + 1, inEnd)

        return root



        

        