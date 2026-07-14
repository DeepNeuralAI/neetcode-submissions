class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute Force
        n = len(s)
        maxLen = 0
        l = r = 0

        maxfreq = 0
        count = defaultdict(int)
        
        while r < n:
            count[s[r]] += 1
            maxfreq = max(maxfreq, count[s[r]])

            if (r - l + 1) - maxfreq > k:
                count[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, (r - l + 1))
            r += 1
        
        return maxLen
            
