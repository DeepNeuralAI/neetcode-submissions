class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.solve(s, 0, [], res)
        return res
        
    def solve(self, s, start, path, res):
        if start == len(s):
            res.append(path.copy())
            return
        
        for end in range(start, len(s)):
            if self.isPalindrome(s, start, end):
                path.append(s[start: end + 1])
                self.solve(s, end + 1, path, res)
                path.pop()

            


    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        