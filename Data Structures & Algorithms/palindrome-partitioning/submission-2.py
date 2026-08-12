class Solution:
    def partition(self, s: str) -> List[List[str]]:
        curr, res = [], []

        def backtrack(start):
            if start == len(s):
                res.append(curr.copy())
                return
            
            for i in range(start, len(s)):
                if self.isPalindrome(s, start, i):
                    curr.append(s[start : i + 1])
                    backtrack(i + 1)
                    curr.pop()
        
        backtrack(0)
        return res
    

    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
        return True
        