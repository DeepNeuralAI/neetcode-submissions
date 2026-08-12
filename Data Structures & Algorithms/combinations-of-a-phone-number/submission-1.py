class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or len(digits) == 0:
            return []
        
        digit_to_char_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        curr, res = [], []

        def backtrack(i):
            if i == len(digits):
                res.append(''.join(curr))
                return
            
            for c in digit_to_char_map[digits[i]]:
                curr.append(c)
                backtrack(i + 1)
                curr.pop()
        
        backtrack(0)
        return res

            

