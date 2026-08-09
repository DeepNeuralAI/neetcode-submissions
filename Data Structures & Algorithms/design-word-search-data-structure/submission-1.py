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
        def dfs(i, node):
            curr = node

            if i == len(word):
                return node.endOfWord
            
            if word[i] == '.':
                for letter in curr.children.values():
                    if dfs(i + 1, letter):
                        return True
                return False
            else:
                if word[i] not in curr.children:
                    return False
                
                return dfs(i + 1, curr.children[word[i]])
           
        return dfs(0, self.root)
            
        
