class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_to_index = { c : i for i, c in enumerate(order)}
        n = len(words)

        for i in range(n - 1):
            first, second = words[i], words[i + 1]
            for j in range(len(first)):
                if j == len(second):
                    return False
                
                if first[j] != second[j]:
                    if char_to_index[second[j]] < char_to_index[first[j]]:
                        return False
                    break
        
        return True

        