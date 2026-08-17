class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_to_idx = {}
        for idx, c in enumerate(order):
            char_to_idx[c] = idx
        
        n = len(words)

        for i in range(n - 1):
            first = words[i]
            second = words[i + 1]

            j = 0
            while j < len(first) and j < len(second):
                if first[j] != second[j]:
                    if char_to_idx[first[j]] > char_to_idx[second[j]]:
                        return False
                    break
                j += 1
            
            if j == len(second) and len(first) > len(second):
                return False
        
        return True
                




        