class TrieNode:
    def __init__(self):
        self.children = {}
        self.iseow = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.iseow = True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.addWord(word)
        curr = trie.root
        m = len(board)
        n = len(board[0])
        ans = []

        for i in range(m):
            for j in range(n):
                self.dfs(curr, board, i, j, m, n, "", ans)
        return ans

    def dfs(self, node, board, i, j, m, n, word, ans):
        if node.iseow:
            ans.append(word)
            node.iseow = False

        if i < 0 or i >= m or j < 0 or j >= n:
            return

        c = board[i][j]
        if c not in node.children:
            return

        board[i][j] = '*'
        self.dfs(node.children[c], board, i, j+1, m, n, word+c, ans)
        self.dfs(node.children[c], board, i, j-1, m, n, word+c, ans)
        self.dfs(node.children[c], board, i+1, j, m, n, word+c, ans)
        self.dfs(node.children[c], board, i-1, j, m, n, word+c, ans)
        board[i][j] = c



    #     m = len(board)
    #     n = len(board[0])
    #     ans = []
    #     visited = [[False] * n for _ in range(m)]

    #     for word in words:
    #         for i in range(m):
    #             if word in ans:
    #                 break
    #             for j in range(n):
    #                 if board[i][j] == word[0]:
    #                     if self.dfs(i, j, m, n, board, word, visited):
    #                         ans.append(word)
    #                         break

    #     return ans
    
    # def dfs(self, i, j, m, n, board, word, visited):
    #     if not word:
    #         return True

    #     if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or board[i][j] != word[0]:
    #         return False
        
    #     visited[i][j] = True
    #     right = self.dfs(i, j+1, m, n, board, word[1:], visited)
    #     left = self.dfs(i, j-1, m, n, board, word[1:], visited)
    #     up = self.dfs(i-1, j, m, n, board, word[1:], visited)
    #     down = self.dfs(i+1, j, m, n, board, word[1:], visited)
    #     visited[i][j] = False

    #     return right or left or up or down

