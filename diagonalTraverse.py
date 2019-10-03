class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or len(matrix)==0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        result = [None] * m * n
        dirs = [[-1,1],[1,-1]]
        row,col,d=0,0,0
        for i in range(m*n):
            result[i] = matrix[row][col]
            row += dirs[d][0]
            col += dirs[d][1]
            if (row >= m):
                row = m - 1
                col += 2
                d = 1 - d
            if (col >= n):
                col = n - 1
                row += 2
                d = 1 - d
            if (row < 0):
                row = 0
                d = 1 - d
            if (col < 0):
                col = 0
                d = 1 - d
        return result
sol = Solution()
print (sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))