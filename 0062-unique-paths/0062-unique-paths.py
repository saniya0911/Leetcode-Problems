class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n]*m
        for i in range(m):
            dp[i][0] = 1

        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp)
        return dp[m-1][n-1]
    #     ans = 0
    #     ans += self.solve(0,0, m, n, ans)
    #     return ans
    
    # def solve(self, row, col, m, n, count):
    #     if row >= m-1 and col >= n-1:
    #         return 1
    #     if row >= m-1:
    #         count += count + self.solve(row, col+1, m, n, count)
    #     elif col >= n-1:
    #         count += count + self.solve(row+1, col, m, n, count)
    #     else:
    #         bottom = count + self.solve(row+1, col, m, n, count)
    #         right = count + self.solve(row, col+1, m, n, count)
    #         count += bottom + right
    #     return count
    