class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_graph = self.build_graph(rowConditions)
        col_graph = self.build_graph(colConditions)

        row_order = self.topological_sort(k, row_graph)
        col_order = self.topological_sort(k, col_graph)

        if not row_order or not col_order:
            return []
        
        index_row_order = {num: i for i, num in enumerate(row_order)}
        index_col_order = {num: i for i, num in enumerate(col_order)}

        grid = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            r, c = index_row_order[num], index_col_order[num]
            grid[r][c] = num
        
        return grid


    def build_graph(self, edges):
        graph = defaultdict(list)

        for src, dst in edges:
            graph[src].append(dst)
        return graph
    

    def topological_sort(self, k, graph):
        ordering = []
        visited = set()
        path = set()
        
        def dfs(node):
            if node in path:
                return False
            
            if node in visited:
                return True

            visited.add(node)
            path.add(node)
            
            for adj in graph[node]:
                if not dfs(adj):
                    return False
                
            ordering.append(node)
            path.remove(node)
            return True

        for num in range(1, k + 1):
            if not dfs(num):
                return []
        
        ordering.reverse()
        return ordering

