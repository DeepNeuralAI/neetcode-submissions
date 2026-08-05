class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return []
        
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.solve(0, [], digits, res, digitToChar)
        return res


    def solve(self, i, current, digits, res, mapping):
        if i == len(digits):
            res.append(''.join(current))
            return
        
        for letter in mapping[digits[i]]:
            current.append(letter)
            self.solve(i + 1, current, digits, res, mapping)
            current.pop()
        
    
        