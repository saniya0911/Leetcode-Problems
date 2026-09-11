class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]
        right = 1
        for i in range(n-1, -1, -1):
            ans[i] = ans[i] * right
            right = right * nums[i]
        return ans
        # n = len(nums)
        # left = [1] * n
        # right = [1] * n
        # for i in range(1, n):
        #     left[i] = left[i-1] * nums[i-1]
        # for j in range(n-2, -1, -1):
        #     right[j] = right[j+1] * nums[j+1]

        # ans = [1] * n
        # for i in range(n):
        #     ans[i] = left[i] * right[i]

        # return ans