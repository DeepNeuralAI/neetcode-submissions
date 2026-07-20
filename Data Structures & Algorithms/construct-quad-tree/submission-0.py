"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        return self.dfs(grid, n, 0, 0)
    


    def dfs(self, grid, n, r, c):
        allSame = True

        for i in range(n):
            for j in range(n):
                if grid[i + r][j + c] != grid[r][c]:
                    allSame = False
                    break
        
        if allSame:
            return Node(grid[r][c], True, None, None, None, None)
        
        n = n // 2
        topLeft = self.dfs(grid, n, r, c)
        topRight = self.dfs(grid, n, r, c + n)
        bottomLeft = self.dfs(grid, n, r + n, c)
        bottomRight = self.dfs(grid, n, r + n, c + n)

        return Node(grid[r][c], False, topLeft, topRight, bottomLeft, bottomRight)
        



        