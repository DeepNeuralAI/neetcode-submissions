class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            s_len = len(s)
            res += f'{s_len}#{s}'
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = j = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            word_len = int(s[i:j])
            res.append(s[(j + 1) : (j + 1) + word_len])
            i = (j + 1 + word_len)
        return res



