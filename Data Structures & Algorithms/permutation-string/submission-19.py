class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        n = len(s2)
        count = defaultdict(int)
        window = defaultdict(int)

        for i in range(len(s1)):
            count[s1[i]] += 1
            window[s2[i]] += 1
        
        num_conditions = len(count)
        matches = 0

        for k, v in count.items():
            if window.get(k, 0) == v:
                matches += 1
        
        if matches == num_conditions:
            return True
        
        l = 0
        r = len(s1)
        """
        s1="aabb"
        s2="baba"
        count = {a: 2, b: 2}
        """
        while r < n:
            window[s2[r]] += 1

            if window[s2[r]] == count.get(s2[r]):
                matches += 1
            elif window[s2[r]] - 1 == count.get(s2[r]):
                matches -= 1
            
            window[s2[l]] -= 1
            if window[s2[l]] == count.get(s2[l]):
                matches += 1
            elif window[s2[l]] + 1 == count.get(s2[l]):
                matches -= 1

            if matches == num_conditions:
                return True

            r += 1
            l += 1
        
        return False




        
        