class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        # Brute Force
        n = len(s1)
        m = len(s2)
        count1 = defaultdict(int)

        for c in s1:
            count1[c] += 1
        
        require = len(count1)
        
        for i in range(m - n + 1):
            window = defaultdict(int)
            met = 0
            for j in range(i, i + n):
                char = s2[j]
                if char in count1:
                    window[char] += 1

                    if window[char] == count1[char]:
                        met += 1
                else:
                    break
            if met == require:
                return True
        return False
        