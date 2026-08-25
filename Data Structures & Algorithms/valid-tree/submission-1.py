class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        graph = self.getAdjList(edges)
        
        def dfs(node, prev = None):
            if node is None:
                return True
            
            visited.add(node)
            for adj in graph[node]:
                if adj == prev:
                    continue
                
                if adj in visited:
                    return False
                
                if not dfs(adj, node):
                    return False
            
            return True
        
        
        if not dfs(0):
            return False
        
        return len(visited) == n
    

    def getAdjList(self, edges):
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        return graph    