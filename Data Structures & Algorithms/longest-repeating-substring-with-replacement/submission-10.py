class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        maxLen = 0

        for i in range(n):
            count = defaultdict(int)
            maxFreq = 0
            
            for j in range(i, n):
                count[s[j]] += 1
                maxFreq = max(count[s[j]], maxFreq)

                if (j - i + 1) - maxFreq <= k:
                    maxLen = max(maxLen, j - i + 1)
        return maxLen

        