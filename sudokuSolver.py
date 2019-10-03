class Solution2(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        print (board)
        self.recurse(board, 0, 0)
        print (board)

    def recurse(self, board, row, col):
        if col == len(board[0]):
            col = 0
            row += 1
        for r in range(row, len(board)):
            for c in range(col, len(board[0])):
                if board[r][c] != '.':
                    continue
                for i in range(1, 10):
                    if self.valid(board, r, c, str(i)):
                        board[r][c] = str(i)
                        if self.recurse(board, row, col + 1):
                            return True
                        board[r][c] = '.'
                return False
        return True

    def valid(self, board, row, col, char):
        for i in range(9):
            if board[row][i] == char or board[i][col] == char:
                return False
        rowOffset = row - row % 3
        colOffset = col - col % 3
        for r in range(3):
            for c in range(3):
                if board[r + rowOffset][c + colOffset] == char:
                    return False
        return True


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.

        Time: O(9^M), where M is number of empty cells.
        Space: O(1)

        Backtracking: For every empty cell, try filling it with 0 to 9, as long as it's legal. Then for each try,
        go onto next empty cell and do the same.
        As soon as a cell has no legal value, leave it as empty, and try the next number in the previous cell.
        When all cells are filled with legal values, the solution is found.
        """
        self.traverse(0, 0, board)
        pass

    def isLegal(self, r, c, board, item):

        for i in range(9):
            if board[r][i] == item:
                return False
            if board[i][c] == item:
                return False

        row, col = r - r % 3, c - c % 3  # Force any actual row,col number into 0 or 3 or 6, start of each small square
        for r in range(3):
            for c in range(3):
                if board[r + row][c + col] == item:
                    return False
        return True

    def traverse(self, r, c, board):
        if r == 9:
            return True
        if c == 9:
            return self.traverse(r + 1, 0, board)
        if board[r][c] != '.':
            return self.traverse(r, c + 1, board)
        for i in range(1, 10):
            item = str(i)
            if self.isLegal(r, c, board, item):
                board[r][c] = item
                if self.traverse(r, c + 1, board):
                    return True
                board[r][c] = '.'
        return False

sol = Solution2()
print (sol.solveSudoku([["5","3",".",".","7",".",".",".","."],
                        ["6",".",".","1","9","5",".",".","."],
                        [".","9","8",".",".",".",".","6","."],
                        ["8",".",".",".","6",".",".",".","3"],
                        ["4",".",".","8",".","3",".",".","1"],
                        ["7",".",".",".","2",".",".",".","6"],
                        [".","6",".",".",".",".","2","8","."],
                        [".",".",".","4","1","9",".",".","5"],
                        [".",".",".",".","8",".",".","7","9"]]))