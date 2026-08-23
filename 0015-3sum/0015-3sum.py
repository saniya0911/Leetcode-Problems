class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        length = len(nums)
        ans = []
        nums.sort()
        for i in range(0, length):
            if (i>0 and nums[i]==nums[i-1]):
                continue
            left = i+1
            right = length -1
            while(left<right):
                s = nums[left] + nums[right] + nums[i]
                if (s == 0):
                    ans.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                    while nums[left] == nums[left-1] and left<right:
                        left+=1
                elif (s < 0):
                    left+=1
                else:
                    right-=1
        return ans