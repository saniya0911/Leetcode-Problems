class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')
        l = 0
        total = 0
        min_len = INF
        ans = INF

        dp = [inf] * n
        for r in range(n):
            total += arr[r]
            while total > target:
                total -= arr[l]
                l += 1
            if total == target:
                curr_len = r - l + 1
                if l > 0 and dp[l-1] != INF:
                    ans = min(ans, dp[l-1] + curr_len)
                min_len = min(min_len, curr_len)
            dp[r] = min(dp[r-1] if r > 0 else INF, min_len)
        return -1 if ans == INF else ans