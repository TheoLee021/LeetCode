class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        # Get the Size of Matrix
        ROWS, COLS = len(matrix), len(matrix[0])
        # Create a new empty matrix for Sum Matrix
        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        # Map the Sum Matrix
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1]
                self.sumMat[r + 1][c + 1] = prefix + above


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # Convert rows and cols for sumMat
        r1, r2, c1, c2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1

        # Set 4 Points to Calculate
        bottomRight = self.sumMat[r2][c2]
        above = self.sumMat[r1 - 1][c2]
        left = self.sumMat[r2][c1 - 1]
        topLeft = self.sumMat[r1 - 1][c1 - 1]

        # Calculation
        return bottomRight - above - left + topLeft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)