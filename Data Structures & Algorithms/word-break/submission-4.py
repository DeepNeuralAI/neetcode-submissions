class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)

        def is_valid(s, start, memo):
            if start == len(s):
                return True
            
            if start in memo:
                return memo[start]
            
            for end in range(start, len(s)):
                if s[start : end + 1] in wordDict:
                    if is_valid(s, end + 1, memo):
                        memo[start] = True
                        return True
            
            memo[start] = False
            return memo[start]
        

        return is_valid(s, 0, {})

       