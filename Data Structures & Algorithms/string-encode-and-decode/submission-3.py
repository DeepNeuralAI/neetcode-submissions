class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f'{len(s)}#{s}'
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        n = len(s)
        i = 0
        
        while i < n:  
            j = i
            
            while j < n and s[j] != '#':
                j += 1
            
            length = int(s[i : j])
            j += 1
            res.append(s[j : j + length])
            i = j + length
        
        return res


