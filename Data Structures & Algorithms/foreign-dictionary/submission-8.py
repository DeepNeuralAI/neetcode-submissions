class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c: set() for word in words for c in word}

        for i in range(1, len(words)):
            prev_word = words[i - 1]
            curr_word = words[i]
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
           
            visited.add(node)
            curr_path.add(node)

            for adj in adjList.get(node, []):
                if adj in curr_path:
                    return False
                
                if adj in visited:
                    continue
                    
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
        


        