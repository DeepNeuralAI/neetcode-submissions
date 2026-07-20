class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Brute Force
        res = ""
        s = strs[0]

        for i in range(len(s)):
            for word in strs[1:]:
                if i == len(word) or word[i] != s[i]:
                    return res
            res += s[i]
        return res
        