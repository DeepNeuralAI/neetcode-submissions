class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Brute Force
        if not strs:
            return ""
        
        n = len(strs)
        m = len(strs[0])

        res = []
        first = strs[0]

        for i in range(m):
            for j in range(1, n):
                word = strs[j]
                if i == len(word) or word[i] != first[i]:
                    return "".join(res)
                
            res.append(first[i])
        
        return "".join(res)
                
                
                
        
             
        