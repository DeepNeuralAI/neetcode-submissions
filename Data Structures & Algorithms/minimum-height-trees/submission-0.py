class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []
        
        if n == 1:
            return [0]
       
        graph = self.buildAdjList(edges)
        degrees = self.getDegrees(n, graph)
        
        def bfs():
            remaining = n
            q = collections.deque()
            
            for node in range(n):
                if degrees[node] == 1:
                    q.append(node)
            
            while q and remaining > 2:
                for _ in range(len(q)):
                    node = q.popleft()
                    remaining -= 1

                    for nei in graph[node]:
                        degrees[nei] -= 1

                        if degrees[nei] == 1:
                            q.append(nei)
            
            return list(q)

        return bfs()


    def buildAdjList(self, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph
    

    def getDegrees(self, n, graph):
        degrees = [0] * n
        
        for node in graph:
            degrees[node] = len(graph[node])
        return degrees

    

   

