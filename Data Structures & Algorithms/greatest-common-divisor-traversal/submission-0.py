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
        
        if self.size[y] <= self.size[x]:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
        else:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]

        self.num_components -= 1
        return True


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        prime_to_num = defaultdict(list)
        uf = UnionFind(len(nums))

        for i, num in enumerate(nums):
            factors = self.findFactors(num)
            for f in factors:
                prime_to_num[f].append(i)
        

        for f, indices in prime_to_num.items():
            base = indices[0]
            for idx in indices[1:]:
                uf.union(base, idx)
        
        return uf.num_components == 1
    
    def findFactors(self, num):
        factors = set()
        f = 2

        while f * f <= num:
            if num % f == 0:
                factors.add(f)
                while num % f == 0:
                    num = num // f
            f += 1
        
        if num > 1:
            factors.add(num)
        
        return factors

        