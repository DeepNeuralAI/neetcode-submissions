class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        maxLen = 0
        count = defaultdict(int)
        maxFreq = 0

        l = r = 0
        while r < n:
            count[s[r]] += 1
            maxFreq = max(count[s[r]], maxFreq)
            
            if (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            
            maxLen = max(maxLen, r - l + 1)
            r += 1
        
        return maxLen


        