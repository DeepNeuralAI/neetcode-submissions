class Solution:
    def validPalindrome(self, s: str) -> bool:
       n = len(s)
       l = 0
       r = n - 1
       
       while l < r:
            if s[l] != s[r]:
                return (self.isPalindrome(s, l + 1, r) or 
                        self.isPalindrome(s, l, r - 1))
            
            l += 1
            r -= 1
        
       return True

    def isPalindrome(self, s, i, j):
        n = len(s)

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
            