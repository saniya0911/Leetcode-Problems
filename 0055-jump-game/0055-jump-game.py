class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        n = len(nums)
        dp = [False] * n
        dp[n-1] = True
        for i in range(n-2, -1, -1):
            if nums[i] >= n-1 - i:
                dp[i] = True
            else:
                for j in range(i+1, i + nums[i] + 1):
                    if j >= n:
                        break
                    
                    if dp[j] == True:
                        dp[i] = True
                        break
        return dp[0]