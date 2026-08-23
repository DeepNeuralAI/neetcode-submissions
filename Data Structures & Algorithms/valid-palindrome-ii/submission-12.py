class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                l_shift = self.isPalindrome(s, l + 1, r)
                r_shift = self.isPalindrome(s, l, r - 1)
                return l_shift or r_shift
            else:
                l += 1
                r -= 1
        return True
    

    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        