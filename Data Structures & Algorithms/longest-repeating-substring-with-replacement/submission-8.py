class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding Window
        maxLen = 0
        
        l = r = 0
        count = {}
        maxFreq = 0
        
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(maxFreq, count[s[r]])
            
            if (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            
            maxLen = max(r - l + 1, maxLen)
            r += 1
        return maxLen