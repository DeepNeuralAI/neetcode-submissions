import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = self.buildAdjList(points)
        heap = []
        heapq.heappush(heap, (0, 0))
        total = 0
        visited = set()
        
        while heap:
            cost, i = heapq.heappop(heap)

            if i not in visited:
                visited.add(i)
                total += cost

                for cost, adj in graph[i]:
                    if adj not in visited:
                        heapq.heappush(heap, (cost, adj))
        return total


    def buildAdjList(self, points):
        adjList = defaultdict(list)
        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(i + 1, len(points)):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))
        return adjList


