class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        curr.endOfWord = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = PrefixTree()
        
        for word in dictionary:
            trie.insert(word)
        
        cache = {}

        def solve(i):
            if i == len(s):
                return 0
            
            if i in cache:
                return cache[i]
            
            res = 1 + solve(i + 1)

            curr = trie.root
            
            for j in range(i, len(s)):
                if s[j] in curr.children:
                    curr = curr.children[s[j]]

                    if curr.endOfWord:
                        res = min(res, solve(j + 1))
                else:
                    break
            
            cache[i] = res
            return res
        
        return solve(0)





        