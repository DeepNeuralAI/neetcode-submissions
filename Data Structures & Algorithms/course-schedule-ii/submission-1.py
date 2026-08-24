class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ordering = []
        stack = []
        visited = set()
        path = []

       

        def dfs(node):
            if node is None:
                return True
            
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
        
        graph = self.getAdjList(prerequisites)

        for node in range(numCourses):
            if node not in visited:
                if not dfs(node):
                    return []
        
        while stack:
            ordering.append(stack.pop())

        return ordering    

    def getAdjList(self, edges):
        graph = defaultdict(list)
        for dst, src in edges:
            graph[src].append(dst)
        return graph