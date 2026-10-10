class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def operations(i, j, memo):
            if j == len(word2):
                return len(word1) - i
            
            if i == len(word1):
                return len(word2) - j
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if word1[i] == word2[j]:
                return operations(i + 1, j + 1, memo)
            
            insert = operations(i, j + 1, memo)
            delete = operations(i + 1, j, memo)
            replace = operations(i + 1, j + 1, memo)

            memo[(i, j)] = 1 + min(insert, delete, replace)
            return memo[(i, j)]
        
        return operations(0, 0, {})
            

            

        