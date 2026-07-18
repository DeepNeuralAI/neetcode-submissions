class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window
        n = len(s)
        maxLen = 0

        l = r = 0
        window = {}
        while r < n:
            if s[r] in window:
                l = max(window[s[r]] + 1, l)
            
            window[s[r]] = r
            maxLen = max(maxLen, r - l + 1)
            r += 1
        
        return maxLen


