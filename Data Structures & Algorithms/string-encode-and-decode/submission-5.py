class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(
                f'{len(s)}#{s}'
            )
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        i = j = 0
        res = []
        n = len(s)

        while j < n:
            i = j
            
            while j < n and s[j] != '#':
                j += 1
            
            length = int(s[i : j])
            j += 1
            res.append(s[j : j + length])
            j = j + length
        
        return res