class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            key = self.getKey(s)
            groups[key].append(s)
        
        return list(groups.values())

    def getKey(self, s):
        key = [0] * 26
        
        for c in s:
            idx = ord(c) - ord('a')
            key[idx] += 1
        
        return tuple(key)