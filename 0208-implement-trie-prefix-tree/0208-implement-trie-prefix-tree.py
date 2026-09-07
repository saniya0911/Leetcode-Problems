class TrieNode:
    def __init__(self):
        self.children = [''] * 26
        self.iseow = False
        
class Trie:

    def __init__(self):
        # self.trie = []
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # self.trie.append(word)
        curr = self.root

        for c in word:
            if not curr.children[ord(c)-ord('a')]:
                curr.children[ord(c)-ord('a')] = TrieNode()
            curr = curr.children[ord(c)-ord('a')]
        curr.iseow = True

    def search(self, word: str) -> bool:
        # if word in self.trie:
        #     return True
        # return False
        curr = self.root
        for c in word:
            if not curr.children[ord(c)-ord('a')]:
                return False
            curr = curr.children[ord(c)-ord('a')]

        return curr.iseow

    def startsWith(self, prefix: str) -> bool:
        # n = len(prefix)
        # if n == 0:
        #     return True
        # for i in range(len(self.trie)):
        #     s = self.trie[i]
        #     word = s[0:n]
        #     if word == prefix:
        #         return True

        # return False
        curr = self.root
        for c in prefix:
            if not curr.children[ord(c)-ord('a')]:
                return False
            curr = curr.children[ord(c)-ord('a')]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)