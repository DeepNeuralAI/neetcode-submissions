class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = r = 0
        n = len(s)
        maxFreq = 0
        maxLen = 0

        while r < n:
            count[s[r]] += 1
            maxFreq = max(maxFreq, count[s[r]])

            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, r - l + 1)
            r += 1
        
        return maxLen

        