class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Sorted Approach
        strs.sort()
        word1 = strs[0]
        word2 = strs[len(strs) - 1]
        
        for i in range(len(word1)):
            if i == len(word2) or word1[i] != word2[i]:
                return word1[:i]
        
        return word1

        