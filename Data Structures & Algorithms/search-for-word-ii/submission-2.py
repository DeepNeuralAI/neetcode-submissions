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
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []

        trie = PrefixTree()
        for word in words:
            trie.insert(word)
        
        self.ROWS, self.COLS = len(board), len(board[0])
        visited = set()
        res = []


        def solve(r, c, node, current):

            char = board[r][c]

            if char not in node.children:
                return

            node = node.children[char]
            
            current.append(char)
            visited.add((r, c))

            if node.endOfWord:
                res.append(''.join(current))
                node.endOfWord = False
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r_ = r + dr
                c_ = c + dc
                
                if self.isValid(r_, c_) and (r_, c_) not in visited:
                    solve(r_, c_, node, current)

            current.pop()
            visited.remove((r, c))
     

        for r in range(self.ROWS):
            for c in range(self.COLS):
                solve(r, c, trie.root, [])
    
        return res
    
    def isValid(self, r, c):
        return 0 <= r < self.ROWS and 0 <= c < self.COLS















