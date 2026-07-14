class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window
        n = len(s)
        mp = {}
        maxLen = 0
        l = r = 0

        while r < n:
            if s[r] in mp:
                if mp[s[r]] >= l:
                    l = mp[s[r]] + 1
            mp[s[r]] = r
            maxLen = max(maxLen, r - l + 1)
            r += 1
        
        return maxLen