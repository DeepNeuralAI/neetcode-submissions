class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            prev_word = words[i]
            curr_word = words[i + 1]
            for j, c in enumerate(prev_word):
                if j == len(curr_word):
                    return ""
                
                if c != curr_word[j]:
                    adjList[c].add(curr_word[j])
                    break
                

        # Topological Sort
        stack = []
        visited = set()
        
        def dfs(node, curr_path):
            if node in curr_path:
                return False
            
            if node in visited:
                return True
           
            visited.add(node)
            curr_path.add(node)

            for adj in adjList.get(node, []):
                if not dfs(adj, curr_path):
                    return False
            
            stack.append(node)
            curr_path.remove(node)
            return True
        
        for c in adjList:
            if c not in visited:
                if not dfs(c, set()):
                    return ""
        
        stack.reverse()
        return ''.join(stack)
        


        