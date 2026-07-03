class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        n = len(strs)
        strs.sort()
        res = ""
        
        s1, s2 = strs[0], strs[n - 1]
        for i in range(len(s1)):
            if i >= len(s2) or s2[i] != s1[i]:
                return res
            res += s1[i]
        
        return res
        