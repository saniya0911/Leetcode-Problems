class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp_first_ex = [0] * (n+2)
        for i in range(1, n):
            dp_first_ex[i+2] = max(dp_first_ex[i+1], dp_first_ex[i]+nums[i])

        dp_last_ex = [0] * (n+2)
        for i in range(0, n-1):
            dp_last_ex[i+2] = max(dp_last_ex[i+1], dp_last_ex[i] + nums[i])

        return max(dp_first_ex[-1], dp_last_ex[-2])