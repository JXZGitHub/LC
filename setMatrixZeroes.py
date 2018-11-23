class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.

        Time: O(M*N)
        Space: O(1)
        """
        firstRowHasZeroes = False
        firstColHasZeroes = False

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    if r == 0:
                        firstRowHasZeroes = True
                    if c == 0:
                        firstColHasZeroes = True
                    matrix[0][c] = 0  # Set the correct cell on the top border row to be 0.
                    matrix[r][0] = 0  # Set the correct cell on the top border col to be 0.

        #Scan again but exclude the top and left most borders this time,
        #zero any cell that has a 0 in its top or left most border.
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[r])):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
                    # IF a cell's row or cols's first element is 0, then this cell must be zero
                    # as it's in the same row or col

        # Finally fill the rest of the first row and cell to be 0's as those were missed above.
        if firstRowHasZeroes:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0

        if firstColHasZeroes:
            for r in range(len(matrix)):
                matrix[r][0] = 0


class Solution_non_constant_space_solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.

        Time: O(M*N)
        Space: O(M+N)
        """
        cols, rows = set(), set()
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    cols.add(c)
                    rows.add(r)

        for c in cols:
            for r in range(len(matrix)):
                matrix[r][c] = 0

        for r in rows:
            for c in range(len(matrix[r])):
                matrix[r][c] = 0
