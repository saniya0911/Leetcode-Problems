class TrieNode:
    def __init__(self):
        self.children = {}
        self.iseow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.iseow = True

    def search(self, word: str) -> bool:
        return self.dfs(word, self.root)
        # curr = self.root
        # for i in range(len(word)):
        #     c = word[i]
        #     if c == '.':
        #         for ch in curr.children:
        #             if self.dfs(word[i+1:], curr.children[ch]):
        #                 return True
        #         return False

        #     elif c not in curr.children:
        #         return False
        #     curr = curr.children[c]
        # return curr.iseow   

    def dfs(self, word, curr):
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for ch in curr.children:
                    if self.dfs(word[i+1:], curr.children[ch]):
                        return True
                return False

            elif c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.iseow   
        # if not word:
        #     return curr.iseow
        # if curr.iseow:
        #     return False
        # if word[0] == '.':
        #     for ch in curr.children:
        #         if self.dfs(word[1:], curr.children[ch]):
        #             return True
        #         return False
        # if word[0] not in curr.children:
        #     return False
        # return self.dfs(word[1:], curr.children[word[0]])

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)