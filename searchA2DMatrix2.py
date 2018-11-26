class Solution_Fast:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        Time :O(m+n), each time either column or row is reduced by 1.
        In the worst case, it keeps reducing on all elements.
        Space: O(1)

        """
        row = len(matrix) - 1
        col = 0
        while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            if target > matrix[row][col]:
                col += 1
            elif target < matrix[row][col]:
                row -= 1
            else:
                return True
        return False


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        Time : no worse than O(n*log(n)) <-- not easy to prove
        Space: O(1)

        Iterate through every diagonal, and perform a Binary Serach on the Row and Column of the diagnoal,
        but only the row and column starting at the currnet diagonal cell. (as the previous numbers have already been
        searched in prev iteration.)
        """
        if not matrix:
            return False
        diagonals = min(len(matrix), len(matrix[0]))
        horizontalEnd = len(matrix[0]) - 1
        verticalEnd = len(matrix) - 1
        for d in range(0, diagonals):  # Treat each diagonal as the starting index of its row and column, starting at 0.
            start = d
            foundInCol = self.binarySearch(start, verticalEnd, matrix, target, True)
            foundInRow = self.binarySearch(start, horizontalEnd, matrix, target, False)
            if foundInCol or foundInRow:
                return True
        return False

    def binarySearch(self, start, end, matrix, target, vertical):
        low = start
        high = end
        while low <= high:
            mid = low + (high - low) // 2
            if vertical:
                value = matrix[mid][start]  # Go vertically on a column.
            else:
                value = matrix[start][mid]  # Go horizontally on a row.
            if target < value:
                high = mid - 1
            elif target > value:
                low = mid + 1
            else:
                return True
        return False



