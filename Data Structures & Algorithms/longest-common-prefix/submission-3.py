class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        m = len(strs)
        n = len(strs[0])
        i = 0
        prefix = ""

        while i < n:
            if strs[0][i] == strs[m - 1][i]:
                prefix += strs[0][i]
                i += 1
            else:
                return prefix

        return prefix