class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        for i in word:
            idx = ord(i) - ord("a")
            if root.children[idx] == None:
                root.children[idx] = TrieNode()
            root = root.children[idx]
        root.endOfWord = True

    def search(self, word: str) -> bool:
        root = self.root
        for i in word:
            idx = ord(i) - ord("a")
            if root.children[idx] == None:
                return False
            root = root.children[idx]
        return root.endOfWord


    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for i in prefix:
            idx = ord(i) - ord("a")
            if root.children[idx] == None:
                return False
            root = root.children[idx]
        return True
        