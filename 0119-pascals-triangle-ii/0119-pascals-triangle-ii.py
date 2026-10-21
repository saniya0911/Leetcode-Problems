class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        ans = [1] * (rowIndex+1)
        for i in range(1, rowIndex+1):
            curr = int(ans[i-1] * (rowIndex-i+1)/i)
            ans[i] = curr
        return ans