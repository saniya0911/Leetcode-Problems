class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        if not word:
            return True
        if m == 0 and n == 0:
            return False

        k = 0
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[k]:
                    if self.dfs(board, word, i, j, k, m, n, visited):
                        return True

        return False

    def dfs(self, board, word, i, j, k, m, n, visited):
        if k >= len(word):
            return True
        if i<0 or i>=m or j < 0 or j >= n or visited[i][j] or board[i][j] != word[k]:
            return False

        visited[i][j] = True
        right = self.dfs(board, word, i, j+1, k+1, m, n, visited)
        down = self.dfs(board, word, i+1, j, k+1, m, n, visited)
        up = self.dfs(board, word, i-1, j, k+1, m, n, visited)
        left = self.dfs(board, word, i, j-1, k+1, m, n, visited)
        visited[i][j] = False

        if right or down or up or left:
            return True

        return False
    