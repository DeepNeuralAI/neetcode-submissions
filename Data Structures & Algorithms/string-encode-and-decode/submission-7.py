class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f'{len(s)}#{s}')
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        l = r = 0
        n = len(s)

        while r < n:
            while s[r] != '#':
                r += 1
            
            word_length = int(s[l : r])
            
            r += 1
            res.append(s[r : r + word_length])
            r = r + word_length
            l = r
        
        return res

