class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.num_components = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False
        
        if self.size[rootY] <= self.size[rootX]:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
        else:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]

        self.num_components -= 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, edge in enumerate(edges):
            edge.append(i)
        
        edges.sort(key = lambda x: x[2])
        
        mst_weight = 0
        uf = UnionFind(n)
        
        for u, v, wt, idx in edges:
            if uf.union(u, v):
                mst_weight += wt
        
        critical, pseudo = [], []

        for u, v, wt, i in edges:
            # Exclude Edge
            new_mst_weight = 0
            num_edges_included = 0
            uf = UnionFind(n)
            
            for u2, v2, wt2, j in edges:
                if i != j and uf.union(u2, v2):
                    new_mst_weight += wt2
                    num_edges_included += 1
            
            if num_edges_included != n - 1 or new_mst_weight > mst_weight:
                critical.append(i)
                continue
                    
            # Force Edge Inclusion
            new_mst_weight = wt
            num_edges_included = 1
            
            uf = UnionFind(n)
            uf.union(u, v)

            for u2, v2, wt2, j in edges:
                if i != j and uf.union(u2, v2):
                    new_mst_weight += wt2
                    num_edges_included += 1
            
            if (num_edges_included == n - 1 and new_mst_weight == mst_weight):
                pseudo.append(i)
        
        return [critical, pseudo]







        