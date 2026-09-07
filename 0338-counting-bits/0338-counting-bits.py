class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            dp[i] = dp[i>>1] + (i&1)
        return dp

    #     ans = []
    #     for i in range(n+1):
    #         ans.append(self.bits(i))
    #     return ans
    
    # def bits(self, i):
    #     count = 0
    #     while i > 0:
    #         count += i & 1
    #         i >>= 1
    #     return count