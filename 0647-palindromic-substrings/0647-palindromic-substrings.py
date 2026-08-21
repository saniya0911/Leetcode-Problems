class Solution:
    def expand(self, s, left, right):
        count = 0
        while(left>=0 and right<len(s) and s[left]==s[right]):
            left = left-1
            right = right+1
            count = count +1
        return count

    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(0, len(s)):
            odd = self.expand(s, i, i)
            even = self.expand(s, i, i+1)
            count += odd + even
        return count