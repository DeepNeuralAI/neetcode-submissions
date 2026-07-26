class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        count = defaultdict(int)
        window = defaultdict(int)

        for i in range(len(s1)):
            count[s1[i]] += 1
            window[s2[i]] += 1
        
        if count == window:
            return True
        
        start = len(s1)
        end = len(s2)

        l = 0
        r = start

        while r < end:
            window[s2[r]] += 1
            window[s2[l]] -= 1

            if window[s2[l]] == 0:
                del window[s2[l]]

            if count == window:
                return True

            r += 1
            l += 1

        return False

        