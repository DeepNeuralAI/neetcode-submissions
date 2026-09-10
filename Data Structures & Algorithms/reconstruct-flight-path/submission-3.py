class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adjList = defaultdict(list)
        
        for i, (src, dst) in enumerate(tickets):
            adjList[src].append((dst, i))

        used = [False] * len(tickets)
        res = []

        def dfs(node):
        
            for dst, i in adjList[node]:
                if used[i]: continue
                used[i] = True
                dfs(dst)
            
            res.append(node)
                

        dfs('JFK')
        return res[::-1]




        