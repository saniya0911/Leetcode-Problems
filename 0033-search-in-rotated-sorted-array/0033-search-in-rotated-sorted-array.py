class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # n = len(nums)
        # ans = -1
        # left = 0
        # right = n-1
        # while(left <= right):
        #     mid = (left+right)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > nums[right]:
        #         # if nums[mid] < target:
        #             if nums[left] <= target:
        #                 right = mid - 1
        #             elif nums[left] > target:
        #                 left = mid + 1
        #         # else:
        #             # if nums[left] < target:
        #             #     right = mid - 1
        #             # elif nums[left] > target:
        #             #     left = mid + 1
        #     elif nums[mid] < nums[right]:
        #         if nums[left] < nums[mid]:
        #             if nums[mid] > target:
        #                 right = mid - 1
        #             else:
        #                 left = mid + 1
        #         else:
        #             if nums[mid] >= target:
        #                 left = mid +1 
        #             else:
        #                 right = mid - 1
        #     # elif nums[mid] > target:
        #     #     right = mid - 1
        #     # else:
        #     #     left = mid + 1
        #     elif left == right:
        #         break
        # return ans
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1