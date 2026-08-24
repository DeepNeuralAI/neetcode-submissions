"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        node_mapping = {}

        def bfs(root):
            q = deque([root])
            node_mapping[root] = Node(root.val)
            
            while q:
                curr = q.popleft()
                
                for adj in curr.neighbors:                    
                    if adj not in node_mapping:
                        node_mapping[adj] = Node(adj.val)
                        q.append(adj)
                    node_mapping[curr].neighbors.append(node_mapping[adj])
        
        bfs(node)        
        return node_mapping[node]

        








        

        

        