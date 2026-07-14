class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding Window
        n = len(s)
        l = r = maxLen = 0
        maxFreq = 0
        count = defaultdict(int)

        while r < n:
            count[s[r]] += 1
            maxFreq = max(maxFreq, count[s[r]])

            if (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            
            maxLen = max(r - l + 1, maxLen)
            r += 1
        
        return maxLen

