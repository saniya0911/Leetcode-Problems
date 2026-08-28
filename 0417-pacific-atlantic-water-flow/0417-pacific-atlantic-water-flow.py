class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]

        for j in range(0,n):
            pacific = self.dfs(m , n, 0, j, pacific, directions, heights)
        for i in range(0,m):
            pacific = self.dfs(m , n, i, 0, pacific, directions, heights)
        for j in range(0,n):
            atlantic = self.dfs(m, n, m-1, j, atlantic, directions, heights)
        for i in range(0,m):
            atlantic = self.dfs(m, n, i, n-1, atlantic, directions, heights)
        return list(pacific & atlantic)

    def dfs(self, m, n,  i, j, visited, directions, heights):
        visited.add((i,j))
        for dx, dy in directions:
            x = i+dx
            y = j+dy
            if 0<= x <m and 0<=y<n:
                if (x,y) not in visited and heights[x][y] >= heights[i][j]:
                    self.dfs(m, n, x, y, visited, directions, heights)

        return visited