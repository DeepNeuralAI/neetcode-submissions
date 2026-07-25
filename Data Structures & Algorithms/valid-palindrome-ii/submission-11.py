class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                lshift = self.isPalindrome(s, l + 1, r)
                rshift = self.isPalindrome(s, l, r - 1)
                return lshift or rshift
        return True    

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        return True
        