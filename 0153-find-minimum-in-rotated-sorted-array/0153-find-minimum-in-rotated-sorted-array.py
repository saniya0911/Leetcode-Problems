class Solution:
    def findMin(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[0]

        # n = len(nums)
        # i = 0
        # while i < n-1 and nums[i] <= nums[i+1]:
        #     i+=1
        # if i == n-1:
        #     return nums[0]
        # return nums[i+1]

        n = len(nums)
        if nums[0] < nums[n-1]:
            return nums[0]

        left = 0
        right = n-1
        x = nums[0]
        while(left <= right):
            mid = (left+right)//2
            if nums[mid] <= nums[left] and nums[mid] <= nums[right]:
                x = min(x, nums[mid])
                right = mid - 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] > nums[left]:
                right = mid - 1

        return x
