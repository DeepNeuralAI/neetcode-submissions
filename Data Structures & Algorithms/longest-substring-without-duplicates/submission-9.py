class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window
        n = len(s)
        charSet = set()
        maxLen = 0
        l = r = 0
        while r < n:
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen