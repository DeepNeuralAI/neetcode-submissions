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

        visited = set()
        node_mapping = {}
        adjList = {}

        def bfs(root):
    
            visited.add(root)
            q = deque([root])

            while q:
                node = q.popleft()
                
                new_node = Node(node.val)
                node_mapping[node.val] = new_node
                adjList[node.val] = []

                for adj in node.neighbors:
                    adjList[node.val].append(adj.val)
                    
                    if adj not in visited:
                        visited.add(adj)
                        q.append(adj)
        
        bfs(node)
        print(adjList)

        for idx in adjList:
            node_copy = node_mapping[idx]
            
            for adj in adjList[idx]:
                adj_copy = node_mapping[adj]
                node_copy.neighbors.append(adj_copy)
        
        return node_mapping[1]

            









        

        

        