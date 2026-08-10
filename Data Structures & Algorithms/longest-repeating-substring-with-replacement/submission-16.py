class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding Window
        n = len(s)
        maxLen = 0

        l = r = 0
        maxFreq = 0
        count = defaultdict(int)

        while r < n:
            count[s[r]] += 1
            maxFreq = max(count[s[r]], maxFreq)
            
            if (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, r - l + 1)
            r += 1
        
        return maxLen
            







        