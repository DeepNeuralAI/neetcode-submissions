import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = self.buildGraph(flights)

        def bfs():
            pq = []
            heapq.heappush(pq, (0, 0, src)) # (dist, number of stops, node)
            visited = set()

            while pq:
                dist, num_stops, node = heapq.heappop(pq)

                if node == dst and num_stops <= k + 1:
                    return dist

                if (num_stops, node) in visited:
                    continue
                
                visited.add((num_stops, node))
                for cost, adj in graph[node]:
                    if num_stops + 1 > k + 1:
                        continue
                    heapq.heappush(pq, (dist + cost, num_stops + 1, adj))

            return -1
        

        return bfs()


    def buildGraph(self, edges):
        adjList = defaultdict(list)

        for src, dst, cost in edges:
            adjList[src].append((cost, dst))
        return adjList
    




        