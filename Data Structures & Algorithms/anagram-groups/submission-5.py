class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            
            key = tuple(key)
            if key not in anagrams:
                anagrams[key] = []
            
            anagrams[key].append(s)
        
        return list(anagrams.values())

        