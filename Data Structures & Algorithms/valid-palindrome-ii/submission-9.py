class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        j = n - 1

        while i <= j:
            if s[i] != s[j]:
                return (self.isPalindrome(s, i + 1, j) or
                        self.isPalindrome(s, i, j - 1))
            i += 1
            j -= 1
        
        return True



    

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        return True
        