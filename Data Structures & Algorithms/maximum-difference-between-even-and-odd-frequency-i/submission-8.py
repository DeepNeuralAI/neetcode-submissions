class Solution:
    def maxDifference(self, s: str) -> int:
        count = defaultdict(int)

        for c in s:
            count[c] += 1
        
        maxDiff = float('-inf')
        oddMax, evenMin = 0, len(s)
        
        for cnt in count.values():
            if cnt % 2 == 0:
                evenMin = min(evenMin, cnt)
            else:
                oddMax = max(oddMax, cnt)
        
        return oddMax - evenMin
        


            
        