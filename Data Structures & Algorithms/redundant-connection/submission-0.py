class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)

        if not edges:
            return []

        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]
        
        return edges[-1]




class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size + 1))
        self.size = [1] * (size + 1)
      

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