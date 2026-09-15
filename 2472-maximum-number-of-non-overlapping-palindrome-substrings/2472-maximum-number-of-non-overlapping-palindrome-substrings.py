class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        end = -1
        ans = 0
        n = len(s)
        for i in range(n):
            for l0 in (i-1, i):
                l = l0
                r = i
                while l >= 0 and r < n and s[l] == s[r]:
                    if r-l+1 >= k and l > end:
                        ans += 1
                        end = r
                        break
                    l -= 1
                    r += 1
        return ans