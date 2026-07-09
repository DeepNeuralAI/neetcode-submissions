class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f'{len(s)}#{s}')
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = j = 0

        while j < len(s):
            while s[j] != '#':
                j += 1
            
            length = int(s[i : j])
            j += 1

            res.append(s[j: j + length])

            j = j + length
            i = j

        return res