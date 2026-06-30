class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Linear Scan
        n = len(arr)
        minIdx = 0
        for i in range(n):
            if abs(arr[i] - x) < abs(arr[minIdx] - x):
                minIdx = i
        
        res = [arr[minIdx]]
        l, r = minIdx - 1, minIdx + 1

        while len(res) < k:
            if l >= 0 and r < n:
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    res.append(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1
            elif l >= 0:
                res.append(arr[l])
                l -= 1
            elif r < n:
                res.append(arr[r])
                r += 1
                
        return sorted(res)

        
        