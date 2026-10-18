class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_order = {c: i for i, c in enumerate(order)}
        n = len(words)

        for i in range(n - 1):
            first = words[i]
            second = words[i + 1]

            for j in range(len(first)):
                if (j == len(second) 
                or char_order[first[j]] > char_order[second[j]]):
                    return False
                
                if first[j] == second[j]:
                    continue
                
                break
        
        return True
                
                
        