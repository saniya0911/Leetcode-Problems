class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        top = 0
        bottom = n -1 
        # vertical reversal
        while top < bottom:
            for j in range(n):
                temp = matrix[top][j]
                matrix[top][j] = matrix[bottom][j]
                matrix[bottom][j] = temp
            top += 1
            bottom -= 1

        # transpose
        for i in range(n):
            for j in range(i, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp