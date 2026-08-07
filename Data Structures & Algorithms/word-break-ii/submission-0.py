class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []

        def backtrack(i, current):
            if i == len(s):
                res.append(' '.join(current))
                return
            
            for end in range(i, len(s)):
                if s[i : end + 1] in wordDict:
                    current.append(s[i : end + 1])
                    backtrack(end + 1, current)
                    current.pop()
            
        backtrack(0, [])
        return res

        