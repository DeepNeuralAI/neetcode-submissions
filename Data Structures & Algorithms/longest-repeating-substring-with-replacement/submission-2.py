class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute Force
        res = 0
        n = len(s)
        maxLen = 0
        
        for i in range(n):
            maxf, count = 0, {}

            for j in range(i, n):
                count[s[j]] = count.get(s[j], 0) + 1
                maxf = max(maxf, count[s[j]])
                length = (j - i + 1) 

                if length - maxf <= k:
                    maxLen = max(maxLen, length)
        return maxLen

        