class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse = True)
        graph = defaultdict(list)

        for src, dst in tickets:
            graph[src].append(dst)
        
        copy = {node : list(graph[node]) for node in graph}
        print(copy)
        def dfs(node):
            while node in copy and copy[node]:
                nei = copy[node].pop()
                dfs(nei)
            res.append(node)
            

        res = []
        dfs('JFK')
        res.reverse()
        return res




        