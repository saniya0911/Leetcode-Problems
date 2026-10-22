class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        return self.merge_sort(nums, 0, n-1)

    def merge_sort(self, nums, left, right):
        if left >= right:
            return 0

        reverse = 0
        mid: int = left + (right - left) // 2

        reverse += self.merge_sort(nums, left, mid)
        reverse += self.merge_sort(nums, mid+1, right)
        reverse += self.merge_and_count(nums, left, mid, right)

        return reverse

    def merge_and_count(self, nums, left, mid, right):
        i = left
        j = mid+1

        merged = []
        count = 0
        while i <= mid and j <= right:
            if nums[i] > 2*nums[j]:
                count += mid-i+1
                j += 1
            else:
                i += 1

        i = left
        j = mid+1

        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                merged.append(nums[i])
                i += 1
            else:
                merged.append(nums[j])
                j += 1

        while i <= mid:
            merged.append(nums[i])
            i += 1

        while j <= right:
            merged.append(nums[j])
            j += 1

        nums[left:right+1] = merged[:]
        return count