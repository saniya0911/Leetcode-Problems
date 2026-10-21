class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            seen = set()
            for j in range(i+1, n-2):
                if nums[j] in seen:
                    continue
                
                left = j+1
                right = n-1
                curr = nums[i] + nums[j]
                while left < right:
                    s = curr + nums[left] + nums[right]
                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                seen.add(nums[j])

        return ans