class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for i in nums:
            if i not in mp:
                mp[i] = 0
            mp[i] += 1

        for key in mp:
            if mp[key] >= 2:
                return True

        return False