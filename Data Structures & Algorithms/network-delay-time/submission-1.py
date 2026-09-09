import heapq as pq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = self.buildAdjList(times)

        def bfs():
            heap = []
            cost = [float('inf')] * (n + 1)
            cost[k] = 0
            pq.heappush(heap, (0, k))
            visited = set()

            while heap:
                t, node = pq.heappop(heap)

                if node in visited:
                    continue
                
                visited.add(node)
                for adj, wt in graph[node]:
                    if adj not in visited:
                        if cost[adj] > wt + t:
                            cost[adj] = wt + t
                            pq.heappush(heap, (cost[adj], adj))
        
            return cost

        dist = bfs()
        res = 0
        for node in range(1, n + 1):
            if dist[node] == float('inf'):
                return -1
            res = max(res, dist[node])
        
        return res
            

                    
                        



    def buildAdjList(self, edges):
        adjList = defaultdict(list)

        for u, v, time in edges:
            adjList[u].append((v, time))
        return adjList