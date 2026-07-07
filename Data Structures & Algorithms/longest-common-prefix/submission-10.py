class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        strs.sort()

        s1, s2 = strs[0], strs[n - 1]

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return s1[:i]
        
        return s1
            


        