class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [1] * n
        # for i in range(1, n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j]+1)
        # return max(dp)
        n = len(nums)
        sub = []
        for i in range(n):
            if not sub or sub[-1] < nums[i]:
                sub.append(nums[i])
            else:
                pos = self.binsearch(sub, nums[i])
                sub[pos] = nums[i]
        return len(sub)

    def binsearch(self, sub, num):
        left = 0
        right = len(sub)-1
        index = 0
        while(left<=right):
            mid = (left+right)//2
            if sub[mid] == num:
                return mid
            elif sub[mid] < num:
                left = mid + 1
            else:
                index = mid
                right = mid - 1
        return index
        ans = self.solve(nums, 0, -inf)
        return ans
    # def solve(self, nums, i, prev):
    #     if i >= len(nums):
    #         return 0
        
    #     dont_take = self.solve(nums, i+1, prev)
    #     take= 0
    #     if nums[i] > prev:
    #         take = 1 + self.solve(nums, i+1, nums[i])
    #     return max(take, dont_take)