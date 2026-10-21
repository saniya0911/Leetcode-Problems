class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        temp1 = [1]
        temp2 = [1, 1]
        ans = []
        if numRows == 0:
            return ans
        ans.append(temp1)
        if numRows == 1:
            return ans
        ans.append(temp2)
        if numRows == 2:
            return ans
        # print(ans)
        for i in range(3, numRows+1):
            temp = []
            temp.append(1)
            # print(temp)
            for j in range(1, i-1):
                curr = ans[i-2][j-1] + ans[i-2][j]
                temp.append(curr)
            temp.append(1)
            ans.append(temp)
        return ans