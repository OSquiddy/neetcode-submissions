class TrieNode():
    def __init__(self):
        self.hashmap = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for idx, char in enumerate(word):
            if char not in current.hashmap:
                current.hashmap[char] = TrieNode()
            current = current.hashmap[char]
        current.isEnd = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.hashmap:
                return False
            current = current.hashmap[char]
        return current.isEnd

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.hashmap:
                return False
            current = current.hashmap[char]
        return True
        
        