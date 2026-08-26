class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.buildAdjList(equations, values)

        def dfs(node, target, cost):
            if node == target:
                return cost
            
            visited.add(node)
            
            for adj, wt in graph[node]:
                if adj not in visited:
                    result = dfs(adj, target, cost * wt)
            
                    if result != -1:
                        return result
            
            return -1
        
        res = []
        for u, v in queries:
            if u not in graph or v not in graph:
                res.append(-1)
                continue
            
            visited = set()
            res.append(dfs(u, v, 1.0))
        
        return res
            
                

    def buildAdjList(self, equations, values):
        adjList = defaultdict(list)
        

        for eq, val in zip(equations, values):
            u, v = eq
            adjList[u].append((v, val))
            adjList[v].append((u,  1 / val))

        return adjList