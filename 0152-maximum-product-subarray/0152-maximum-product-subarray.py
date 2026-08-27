class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_prod = 1
        max_prod = -inf
        n = len(nums)
        for i in range(0,n):
            curr_prod = curr_prod*nums[i]
            max_prod = max(max_prod, curr_prod)
            if curr_prod == 0:
                curr_prod = 1

        curr_prod = 1
        for i in range(n-1, -1, -1):
            curr_prod *= nums[i]
            max_prod = max(max_prod, curr_prod)
            if curr_prod == 0:
                curr_prod = 1

        return max_prod
