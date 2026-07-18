class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:        
        if len(s2) < len(s1):
            return False
        
        # Sliding Window
        n = len(s1)
        m = len(s2)
        count1 = defaultdict(int)
        window = defaultdict(int)

        for i in range(len(s1)):
            count1[s1[i]] += 1
            window[s2[i]] += 1


        required = len(count1)
        met = 0

        for char in count1:
            if window[char] == count1[char]:
                met += 1
        
        if met == required:
            return True
        
        l = 0
        r = n
        while r < m:
           
            
            char_in = s2[r]
            if window[char_in] == count1.get(char_in):
                met -= 1
            
            if window[char_in] + 1 == count1.get(char_in):
                met += 1
            
            window[char_in] += 1
            

            char_out = s2[l]

            if window[char_out] == count1.get(char_out):
                met -= 1
            
            if window[char_out] - 1 == count1.get(char_out):
                met += 1
            
            window[char_out] -= 1

            if met == required:
                return True
            
            l += 1
            r += 1
        
        return False