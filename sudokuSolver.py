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
