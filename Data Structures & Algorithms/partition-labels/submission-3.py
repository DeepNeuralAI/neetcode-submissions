class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdxMap = {c : i for i, c in enumerate(s)}

        l = r = 0
        res = []
        start = end = 0

        for i, c in enumerate(s):
            end = max(end, lastIdxMap[c])

            if i == end:
                res.append(end - start + 1)
                start = end + 1
            
        return res


            


        

        
        