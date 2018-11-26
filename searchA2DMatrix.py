class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        Time: O(log(M*N))
        Space: O(1)

        This problem is similar to searchMatrix 2 -
        Each row is ascending and each column is also ascending (implied) - except every starting number of each row is
        bigger than prev row's ending number.

        Using " every starting number of each row is bigger than prev row's ending number",
        we can flatten the matrix into a one-dimensional array, then do a regular Binary Search on the array.

        Given a matrix of N cols converted to an array of M*N elements, i'th index of the array is equal
        to matrix[i//N][i%N].

        """
        if not matrix or not matrix[0]:
            return False

        start = 0
        numCols = len(matrix[0])
        end = len(matrix) * len(matrix[0]) - 1
        while start <= end:
            mid = start + (end - start) // 2
            row, col = divmod(mid, numCols)  # row = mid//midCols,  col = mid % midCols
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                start = mid + 1
            else:
                end = mid - 1
        return False


class Solution_2_Binary_Search:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        Time: O(log(M)+log(N)) = O(log(M*N))
        Space: O(1)

        This problem is similar to searchMatrix 2 -  Each row is ascending and each column is also ascending (implied)
        - except every starting number of each row is bigger than prev row's ending number.

        So we first use binary search to find the 'left boundary' in the first column to get the row that the target
        may fall into, then do another binary search in that row for target.

        """
        if not matrix or not matrix[0]:
            return False

        start = 0
        end = len(matrix) - 1

        # Binary search for 'left boundary' of target in the first column, which is the last item that's < target,
        # or first item equal to target.

        while start <= end:
            mid = start + (end - start) // 2
            if target <= matrix[mid][0]:
                end = mid - 1
            elif target > matrix[mid][0]:
                start = mid + 1
            if target == matrix[mid][0]:
                return True

        # Now to a regular binary search for an exact match on target.
        rowToSearch = end
        start = 0
        end = len(matrix[rowToSearch]) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if target == matrix[rowToSearch][mid]:
                return True
            elif target > matrix[rowToSearch][mid]:
                start = mid + 1
            else:
                end = mid - 1
        return False