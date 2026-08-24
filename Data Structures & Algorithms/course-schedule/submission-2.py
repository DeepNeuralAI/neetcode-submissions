from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        graph = self.getAdjList(prerequisites)
        indegrees = self.getInDegrees(prerequisites, numCourses)
        
        # Kahns Algorithm - BFS
        
        def bfs():
            q = deque()
            total = 0

            for u, deg in enumerate(indegrees):
                if deg == 0:
                    q.append(u)
                    total += 1
            
            while q:
                node = q.popleft()

                for nei in graph[node]:
                    indegrees[nei] -= 1

                    if indegrees[nei] == 0:
                        q.append(nei)
                        total += 1
            return total
        
        total = bfs()
        return total == numCourses



    def getInDegrees(self, edges, n):
        indegrees = [0] * n
        for dst, src in edges:
            indegrees[dst] += 1
        return indegrees

    def getAdjList(self, edges):
        graph = defaultdict(list)
        for dst, src in edges:
            graph[src].append(dst)
        return graph

        