class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window
        n = len(s)
        maxLen = 0
        window = {}

        l = r = 0
        while r < n:
            if s[r] in window:
                l = max(l, window[s[r]] + 1)
           
            window[s[r]] = r
            maxLen = max(maxLen, r - l + 1)
            r += 1
        
        return maxLen


        