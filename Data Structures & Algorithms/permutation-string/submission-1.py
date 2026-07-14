class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute Force

        if len(s1) > len(s2):
            return False
        
        count1 = defaultdict(int)
        for c in s1:
            count1[c] += 1
        
        need = len(count1)

        for i in range(len(s2)):
            count2 = defaultdict(int)
            cur = 0
            for j in range(i, len(s2)):
                if s2[j] not in count1:
                    break
                
                count2[s2[j]] += 1
                
                if count2[s2[j]] > count1[s2[j]]:
                    break
                elif count2[s2[j]] == count1[s2[j]]:
                    cur += 1
                
                if cur == need:
                    return True
        return False


        