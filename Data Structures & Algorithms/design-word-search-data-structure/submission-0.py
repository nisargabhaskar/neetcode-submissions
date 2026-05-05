class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        root = self.root
        for i in word:
            if i not in root.children:
                root.children[i] = TrieNode()
            root = root.children[i] 
        root.eow = True

    def search(self, word: str) -> bool:
        def dfs(j,root):
            cur = root
            for i in range(j,len(word)):
                if '.' == word[i]:
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if word[i] not in cur.children:
                        return False
                cur = cur.children[word[i]]
            return cur.eow
        return dfs(0,self.root)
            
        
