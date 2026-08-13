class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res, curr = [], []
        wordDict = set(wordDict)

        def backtrack(start):
            if start == len(s):
                res.append(' '.join(curr))
                return
            
            for end in range(start, len(s)):
                if s[start : end + 1] in wordDict:
                    curr.append(s[start : end + 1])
                    backtrack(end + 1)
                    curr.pop()
        
        backtrack(0)
        return res
            


        