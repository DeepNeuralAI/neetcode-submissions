class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        path = []
        stack = []

        graph = self.getAdjList(prerequisites)
        
        def dfs(node):
            visited.add(node)
            path.append(node)

            for nei in graph[node]:
                if nei in path:
                    return False
                
                if nei in visited:
                    continue
                
                if not dfs(nei):
                    return False
            
            stack.append(node)
            path.pop()
            return True
        
        for node in range(numCourses):
            if node not in visited:
                if not dfs(node):
                    return False
        
        return len(stack) == numCourses
    

    def getAdjList(self, edges):
        graph = defaultdict(list)
        for dst, src in edges:
            graph[src].append(dst)
        return graph

        