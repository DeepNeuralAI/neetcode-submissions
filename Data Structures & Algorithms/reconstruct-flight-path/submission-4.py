class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse = True)
        graph = defaultdict(list)

        for src, dst in tickets:
            graph[src].append(dst)
        

        def dfs(node):
            while graph[node]:
                nei = graph[node].pop()
                dfs(nei)
            res.append(node)
            

        res = []
        dfs('JFK')
        res.reverse()
        return res




        