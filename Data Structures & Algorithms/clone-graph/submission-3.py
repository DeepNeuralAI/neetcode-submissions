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

        def dfs(node):
            # For a given node, return copy
            if node in node_mapping:
                return node_mapping[node]
            
            node_mapping[node] = Node(node.val)
            for adj in node.neighbors:
                node_mapping[node].neighbors.append(dfs(adj))
            
            return node_mapping[node]
        

        return dfs(node)

        








        

        

        