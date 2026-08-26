class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        # graph = self.buildAdjList(edges)

        uf = UnionFind(n)
        num_operations = 0
        
        for u, v in edges:
            if uf.union(u, v):
                num_operations += 1
        
        return n - num_operations




class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.size = [1] * size
      

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]

        return True