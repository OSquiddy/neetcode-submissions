class TrieNode:
    def __init__(self, val=0):
        self.val = val
        self.children = {}
        self.isEndOfWord = False



class Solution:

    def buildTrie(self, words):
        root = TrieNode()

        for word in words:
            current = root
            for char in word:
                if current.children.get(char) is None:
                    current.children[char] = TrieNode(char)
                current = current.children[char]
            current.isEndOfWord = True

        return root


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.buildTrie(words)

        rows, cols = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isEndOfWord:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        
        return list(res)