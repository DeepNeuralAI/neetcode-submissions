class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        graph = self.buildAdjList(edges)

        def dfs(node):
            visited.add(node)

            for adj in graph[node]:
                if adj not in visited:
                    dfs(adj)
            
        components = 0
        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)
        return components

    def buildAdjList(self, edges):
        adjList = defaultdict(list)

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        return adjList        