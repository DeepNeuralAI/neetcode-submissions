class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdxMap = {c : i for i, c in enumerate(s)}

        l = r = 0
        res = []

        while r < len(s):
            i = l
            r = lastIdxMap[s[r]]

            while i <= r:
                r = max(r, lastIdxMap[s[i]])
                i += 1
 
            res.append(r - l + 1)
            l = r + 1
            r = l
        
        return res
            


        

        
        