class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n ==1:
            return 1
        prev = 1
        curr = 1
        ans = prev + curr
        for i in range(2,n):
            prev = curr
            curr = ans
            ans = prev + curr
        return ans
        # if n ==0:
        #     return 1
        # if n < 0:
        #     return 0
        # one = 0
        # two = 0
        # one += self.climbStairs(n-1)
        # two += self.climbStairs(n-2)
        # return one + two