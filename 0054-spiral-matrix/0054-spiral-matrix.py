class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        srow = 0
        erow = m
        scol = 0
        ecol = n
        ans = []

        while srow < erow and scol < ecol:
            for j in range(scol, ecol):
                ans.append(matrix[srow][j])
            
            for i in range(srow+1, erow):
                ans.append(matrix[i][ecol-1])
            
            for j in range(ecol - 2, scol-1, -1):
                if srow == erow -1:
                    break
                ans.append(matrix[erow-1][j])

            for i in range(erow-2, srow, -1):
                if scol == ecol - 1:
                    break
                ans.append(matrix[i][scol])

            srow += 1
            erow -= 1
            scol += 1
            ecol -= 1

        return ans