class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # for i in range(0,n):
        #     while nums[i] != i and nums[i] < n:
        #         x = nums[i]
        #         temp = nums[x]
        #         nums[x] = x
        #         nums[i] = temp

        # for i in range(0, n):
        #     if nums[i] != i:
        #         return i

        # return n
        n = len(nums)
        sum = n*(n+1)/2
        s = 0
        for i in range(0,n):
            s +=nums[i]
        if s==sum:
            return 0
        else:
            return int(sum-s)