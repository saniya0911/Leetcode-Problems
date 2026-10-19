class TrieNode:
    def __init__(self):
        self.children = {}
        self.ieow = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.ieow = True   
            
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        tr = Trie()
        for s in strs:
            if not s:
                return ""
            tr.insert(s)
            
        curr = tr.root
        pre = ""
        
        while len(curr.children) == 1 and not curr.ieow:
            c = next(iter(curr.children))
            pre += c
            curr = curr.children[c]
        return pre