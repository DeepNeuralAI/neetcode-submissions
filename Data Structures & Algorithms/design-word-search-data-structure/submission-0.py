class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        curr.endOfWord = True
        
    def search(self, word: str) -> bool:
        def dfs(index, node):
            curr = node

            for i in range(index, len(word)):

                if word[i] == '.':
                    for child in curr.children:
                        if dfs(i + 1, curr.children[child]):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]

            return curr.endOfWord
        
        return dfs(0, self.root)
            
        
