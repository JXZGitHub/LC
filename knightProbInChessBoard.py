class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float

        On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves.

        The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).
        A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal
        direction, then one square in an orthogonal direction.
        Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

        The knight continues moving until it has made exactly K moves or has moved off the chessboard.
        Return the probability that the knight remains on the board after it has stopped moving.

        Input: 3, 2, 0, 0
        Output: 0.0625
        Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
        From each of those positions, there are also two moves that will keep the knight on the board.
        The total probability the knight stays on the board is 0.0625.
        """

        #Let prob be a NxN board represnting probabilty of the knight being here based on a previous board position
        prob = [[0 for _ in range(N)] for _ in range(N)]
        prob[r][c] = 1 #Starting position's probability is 1 by definition.

        for _ in range(K):
            new_prob=[[0 for _ in range(N)] for _ in range(N)] #A fresh new board to start updating from previous board.
            #With each move, visit each cell on grid, and update the probably of each 'destination' cell with the source being the current cell.
            for r,row in enumerate(prob):
                for c,val in enumerate(row):
                    for (dr,dc) in [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]:
                        if 0 <= r + dr < N and 0 <= c + dc < N:  # If each move is Not out of bounds.
                            #The porbably of each desitnaiton cell is 1/8 of the value(probability) of the source from the
                            #previous board (val is from previous 'prob's source cell)
                            new_prob[r+dr][c+dc] += val / 8.0
            prob=new_prob #updated board becomes previous board for next iteration.

        return sum(map(sum,prob)) #Probability of knight remianing on board is total probaility of all of its destination cells after K moves.






