# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        def splitTree(preL, preR, inL, inR):

            if preL > preR:
                return None
            
            root_val = preorder[preL]

            root = TreeNode(root_val)
            mid = inorder_map[root_val]

            left_size = mid - inL

            root.left = splitTree(preL + 1, preL + left_size, inL, mid - 1)
            root.right = splitTree(preL + left_size + 1, preR, mid + 1, inR)

            return root
        

        n = len(preorder)
        root = splitTree(0, n - 1, 0, n - 1)
        return root







