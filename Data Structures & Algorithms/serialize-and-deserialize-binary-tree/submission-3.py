# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        order = self.traverse(root)
        return ','.join(order)
    
    def traverse(self, root):
        res = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node is None:
                res.append('#')
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None
        
        str_nodes = data.split(',')
        n = len(str_nodes)
        root = TreeNode(int(str_nodes[0]))
        queue = deque([root])

        i = 1
        while queue:
            parent = queue.popleft()

            if i < n and str_nodes[i] != '#':
                left = TreeNode(int(str_nodes[i]))
                parent.left = left
                queue.append(left)
            i += 1

            if i < n and str_nodes[i] != '#':
                right = TreeNode(int(str_nodes[i]))
                parent.right = right
                queue.append(right)
            i += 1
        
        return root



                


