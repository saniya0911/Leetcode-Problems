class Solution:
    def findMin(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[0]
        n = len(nums)
        i = 0
        while i < n-1 and nums[i] <= nums[i+1]:
            i+=1
        if i == n-1:
            return nums[0]
        return nums[i+1]