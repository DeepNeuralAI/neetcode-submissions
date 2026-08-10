class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window
        n = len(s)
        l = r = 0
        seen = set()
        maxLen = 0

        while r < n:
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen

