class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pos = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                pos = i
                break

        if pos == -1:
            return nums.reverse()

        suc = pos +1
        for i in range(pos+1, n):
            if nums[i] > nums[pos] and nums[i] <= nums[suc]:
                suc = i

        nums[pos], nums[suc] = nums[suc], nums[pos]
        nums[pos+1:] = reversed(nums[pos+1:])