class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]

        Recursive DFS
        Time: O(M*N)
        Space: O(1) #The returned board, even though a copy, won't count as space usage as it's a return result
        """
        newBoard = [[board[r][c] for c in range(len(board[r]))] for r in range(len(board))]
        self.dfs(newBoard, click[0], click[1])
        return newBoard

    def dfs(self, board, row, col):
        # There's no need to maintain visited cells, because when we visit every cell, its value will never remain 'M' or 'E', and so any repeated visits will not do anything due to if condition only checking for 'M' or 'E'.
        if board[row][col] == 'M':
            board[row][col] = 'X'
        elif board[row][col] == 'E':
            mines = 0
            emptyNeighbors = []
            for (dr, dc) in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
                new_row = row + dr
                new_col = col + dc
                if not (0 <= new_row < len(board) and 0 <= new_col < len(board[0])):
                    continue
                if board[new_row][new_col] == 'M':
                    mines += 1
                else:
                    # Keep track of all the surrounding cells in case no mine is found in any neighbor,
                    # so we don't have to do an identical for loop later to find all surrounding cells.
                    emptyNeighbors.append((new_row, new_col))
            if mines > 0:
                board[row][col] = str(mines)
            else:
                board[row][col] = 'B'
                for new_row, new_col in emptyNeighbors:
                    self.dfs(board, new_row, new_col)


class Solution_BFS:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]

        BFS

        Time: O(M*N)
        Space: O(8) -> O(1) #At most 8 neighbors added to a given cell in the queue.
        """
        newBoard = [[board[r][c] for c in range(len(board[r]))] for r in range(len(board))]
        q = [(click[0], click[1])]
        while q:
            newQ = []
            for row, col in q:
                if newBoard[row][col] == 'M':
                    newBoard[row][col] = 'X'
                    return newBoard
                elif newBoard[row][col] == 'E':
                    mines = 0
                    emptyNeighbors = []
                    for (dr, dc) in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
                        new_row = row + dr
                        new_col = col + dc
                        if not (0 <= new_row < len(board) and 0 <= new_col < len(board[0])):
                            continue
                        if board[new_row][new_col] == 'M':
                            mines += 1
                        else:
                            # Keep track of all the surrounding cells in case no mine is found in any neighbor, so we
                            # don't have to do an identical for loop later to find all surrounding cells.
                            emptyNeighbors.append((new_row,new_col))
                    if mines > 0:
                        newBoard[row][col] = str(mines)
                    else:
                        newBoard[row][col] = 'B'
                        for new_row, new_col in emptyNeighbors:
                            newQ.append((new_row, new_col))
            q = newQ
        return newBoard


sol = Solution()
print (sol.updateBoard([["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]],
[3,0]))