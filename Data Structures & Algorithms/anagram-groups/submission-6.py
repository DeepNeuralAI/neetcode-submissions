class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        key_to_strs = defaultdict(list)

        def get_key(s):
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            return tuple(key)
        

        for s in strs:
            key = get_key(s)
            key_to_strs[key].append(s)
        
        for k, v in key_to_strs.items():
            res.append(v)
        
        return res
        