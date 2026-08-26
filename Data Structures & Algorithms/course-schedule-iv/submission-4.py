class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reachable = defaultdict(set)

        graph = self.getAdjList(prerequisites)
        
        def dfs(node, u):
            if node in reachable[u]:
                return reachable[node]
            
            reachable[u].add(node)
            for adj in graph[node]:
                reachable[u].update(dfs(adj, node))
            return reachable[u]

        for crs in range(numCourses):
            if crs not in reachable:
                dfs(crs, crs)
        
        res = []
        for u, v in queries:
            res.append(v in reachable[u])
        return res


    def getAdjList(self, edges):
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
        return graph    