class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordsList = set(wordList)
        if endWord not in wordList:
            return 0
        
        def bfs():
            q = collections.deque([(beginWord, 1)])
            visited = set([beginWord])

            while q:
                word, d = q.popleft()

                if word == endWord:
                    return d

                tmp = list(word)
                for i in range(len(word)):
                    letter = word[i]
                    for j in range(26):
                        new_letter = chr(j + ord('a'))
                        if new_letter != letter:
                            tmp[i] = new_letter
                        
                        new_word = ''.join(tmp)
                        tmp[i] = letter

                        if new_word in wordList and new_word not in visited:
                            visited.add(new_word)
                            q.append((new_word, d + 1))

            return 0
        
        return bfs()

