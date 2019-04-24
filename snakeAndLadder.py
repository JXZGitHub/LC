class Solution:
    def snakesAndLadders(self, board):
        moves = 0
        dest = [1]
        visited = set()
        while dest:
            moves += 1
            new_dest = []
            for d in dest:
                if d in visited:
                    continue
                visited.add(d)
                if d == len(board) ** 2:
                    return moves
                for i in range(1, 7):
                    if d + i <= len(board) ** 2:
                        next_cell = d + i
                        r, c = self.coord_from_num(board, next_cell)
                        val = board[r][c]
                        if next_cell not in visited:
                            if val != -1:
                                new_dest.append(val)
                            else:
                                new_dest.append(next_cell)
            dest = new_dest

    def coord_from_num(self, board, num):
        n = len(board)
        old_row = (num - 1) // n
        row = n - 1 - old_row
        old_col = (num - 1) % n
        if old_row % 2 == 0:
            col = old_col
        else:
            col = n - 1 - old_col
        return row, col

sol = Solution()
print (sol.snakesAndLadders(board=[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))