class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.

        1)First transpose the matrix (matrix[i][j] = matrix[j][i])
        2)For every row that's transposed, flip along its middle: (swap its first column element with its last column element)

        Time: O(n^2)
        Space: O(1)
        """
        for row in range(len(matrix)):
            for col in range(row, len(
                    matrix[row])):  # Skip already switched cells from previous iteration, otherwise it'll get restored.
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]  # Transpose matrix

            # After all elements are transposed at each row, flip first and last element of row.
            matrix[row] = list(reversed(matrix[row]))
