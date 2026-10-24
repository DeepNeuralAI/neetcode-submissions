class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        res = []
        for s in strs:
            res.append(f'{len(s)}#{s}')
        
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        messages = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            size = int(s[i : j])
            j += 1
            messages.append(s[j : j + size])
            i = j + size
        
        return messages
            

            



