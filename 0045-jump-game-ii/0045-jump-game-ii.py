class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return 0

        jumps = 0
        curr_end = 0
        max_end = 0
        for i in range(n-1):
            max_end = max(max_end, i + nums[i])
            if i == curr_end:
                jumps +=1
                curr_end = max_end
                if curr_end >= n-1:
                    break
        return jumps