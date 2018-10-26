class Solution_verbose:
    def isValidRow(self, row, board):
        seen_row = set()
        for i in range(9):
            cell_row = board[row][i]
            if cell_row != '.' and cell_row in seen_row:
                return False
            seen_row.add(cell_row)
        return True

    def isValidCol(self, col, board):
        seen_col = set()
        for i in range(9):
            cell_col = board[i][col]
            if cell_col != '.' and cell_col in seen_col:
                return False
            seen_col.add(cell_col)
        return True

    def isValidCube(self, rowStart, colStart, board):
        seen_cube = set()
        for r in range(3):
            for c in range(3):
                cell = board[rowStart + r][colStart + c]
                if cell != '.' and cell in seen_cube:
                    return False
                seen_cube.add(cell)
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool

        Time: O(M) where M is number of empty cells.
        Space: O(9+9+9)
        """
        valid_rows, valid_cols, valid_cubes = set(), set(), set()
        for r in range(len(board)):
            for c in range(len(board[r])):
                if r not in valid_rows:
                    if self.isValidRow(r, board):
                        valid_rows.add(r)
                    else:
                        return False
                if c not in valid_cols:
                    if self.isValidCol(c, board):
                        valid_cols.add(c)
                    else:
                        return False

                # (row_start, col_start) is the left most corner of each sub-cube, so it uniquely defines a sub-cube
                row_start = r - r % 3
                col_start = c - c % 3
                if (row_start, col_start) not in valid_cubes:
                    if self.isValidCube(r, c, board):
                        valid_cubes.add((row_start, col_start))
                    else:
                        return False
        return True


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool

        Time: O(M) where M is number of empty cells.
        Space: O(9+9+9)
        """

        for i in range(len(board)):
            valid_rows, valid_cols, valid_cubes = set(), set(), set()
            for j in range(len(board[i])):
                if board[i][j] != '.' and board[i][j] in valid_rows:
                    return False
                if board[j][i] != '.' and board[j][i] in valid_cols:
                    return False
                row_start = i - i % 3
                col_start = j - j % 3
                # row_start = 3*(i//3)
                # col_start = 3*(i%3)
                if board[row_start + j // 3][col_start + j % 3] != '.' and board[row_start + j // 3][
                    col_start + j % 3] in valid_cubes:
                    return False
                valid_rows.add(board[i][j])
                valid_cols.add(board[j][i])
                valid_cubes.add(board[row_start + j // 3][col_start + j % 3])
        return True

sol = Solution()
sol.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])