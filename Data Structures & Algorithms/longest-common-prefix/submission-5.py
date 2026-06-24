class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        minIdx = 0

        for i in range(1, len(strs)):
            if len(strs[i]) < len(strs[minIdx]):
                minIdx = i
        
        word = strs[minIdx]
        trie.insert(word)
        minLen = len(word)

        for i in range(len(strs)):
            prefixLen = trie.lcp(strs[i], len(word))
            minLen = min(prefixLen, minLen)
        return word[:minLen]

class Node:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        
        curr.word = True
    

    def lcp(self, word, maxLen):
        curr = self.root
        for i in range(maxLen):
            if word[i] not in curr.children:
                return i
            curr = curr.children[word[i]]
        
        return maxLen

