class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        ans = []
        for i in range(len(nums)):
            n = nums[i]
            if (target - n) in mp.keys():
                ans.append(mp[target - n])
                ans.append(i)
                return ans
            
            mp[n] = i

        return ans