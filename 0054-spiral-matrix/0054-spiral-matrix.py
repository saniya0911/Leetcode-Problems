class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        srow = 0
        scol = 0
        erow = m
        ecol = n

        temp = []

        while srow<erow and scol<ecol:
            for i in range(scol, ecol):
                temp.append(matrix[srow][i])
            srow += 1
            for i in range(srow, erow):
                temp.append(matrix[i][ecol-1])
            ecol -= 1
            for i in range(ecol-1, scol-1, -1):
                if len(temp) == m*n:
                    break
                temp.append(matrix[erow-1][i])
            erow -= 1
            for i in range(erow-1, srow-1, -1):
                if len(temp) == m*n:
                    break
                temp.append(matrix[i][scol])
            scol += 1
        return temp