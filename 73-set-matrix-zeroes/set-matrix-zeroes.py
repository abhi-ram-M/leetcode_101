class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        row_track = [0]*r
        col_track = [0]*c
        for i in range(r):
            for j in range(c):
                if not matrix[i][j]:
                    row_track[i] = 1
                    col_track[j] = 1
        for i in range(r):
            for j in range(c):
                if row_track[i] or col_track[j]:
                    matrix[i][j] = 0

        