
#All 3 methods are Time: O(R*C).
#They all start at each cell on the borders and keep track of all visited 'O' cells from the border.
#Then any 'O' that is not visited from border will be 'kliled' (turned to X).

#DFS: Space:  Heap O(R*C). Stack O(Max of length or width)
#UF: Space: Heap O(R*C). Stack O(Max of length or width)
#BFS: Space: Heap O(R*C). No stack as it's iterative.

class Solution:
    #Recursive DFS
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        alive,v = set(),set()
        for r in range(len(board)):
            for c in range(len(board[r])):
                if r==0 or r==len(board)-1 or c==0 or c==len(board[0])-1:
                    self.traverse(board,r,c,alive)
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c]=='O' and (r,c) not in alive:
                    board[r][c] = 'X'

    def traverse(self,board,r,c,alive):
        if (r,c) in alive or r<0 or r>len(board)-1 or c<0 or c>len(board[0])-1 or board[r][c] != 'O' :
            return
        else:
            alive.add((r,c))
            self.traverse(board,r+1,c,alive)
            self.traverse(board,r,c+1,alive)
            self.traverse(board,r-1,c,alive)
            self.traverse(board,r,c-1,alive)


class Solution:
    #Union Find.
    def solve(self, board):
        parents = {}
        for r in range(len(board)):
            for c in range(len(board[r])):
                if r == 0 or r == len(board) - 1 or c == 0 or c == len(board[0]) - 1:
                    self.traverse(board, parents, r, c, -1, -1)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == 'O' and parents.get((r, c)) != (-1, -1):
                    board[r][c] = 'X'

    def traverse(self, board, parents, r, c, pr, pc):
        if (r, c) in parents or r < 0 or r > len(board) - 1 or c < 0 or c > len(board[0]) - 1 or board[r][c] != 'O':
            return
        else:
            parentCurr = self.find((r, c), parents)
            parentPrev = self.find((pr, pc), parents)
            if parentCurr != parentPrev:
                parents[parentCurr] = parentPrev
            self.traverse(board, parents, r + 1, c, r, c)
            self.traverse(board, parents, r - 1, c, r, c)
            self.traverse(board, parents, r, c + 1, r, c)
            self.traverse(board, parents, r, c - 1, r, c)

    def find(self, node, parents):
        if node not in parents:
            parents[node] = node
            return node
        if parents[node] != node:
            parents[node] = self.find(parents[node], parents)
        return parents[node]

import collections
class Solution:
    #Iterative BFS
    #Temporarily turn 'reachable O cells form border' into '#', then any '#' is restored to 'O', and any 'O' is changed to 'X'.
    def solve(self,board):
        for r in range(len(board)):
            for c in range(len(board[r])):
                if r==0 or r==len(board)-1 or c==0 or c==len(board[0])-1:
                    self.traverse(board,r,c)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c]=='O':
                    board[r][c] = 'X'
                elif board[r][c]=='#':
                    board[r][c] = 'O'

    def traverse(self,board,r,c):
        q=collections.deque()
        if board[r][c]=='O':
            q.append((r,c))
        while q:
            c = q.popleft()
            r,c=c[0],c[1]
            if r>=0 and r<len(board) and c>=0 and c<len(board[0]) and board[r][c]=='O':
                board[r][c]='#'
                q.append((r+1,c))
                q.append((r-1,c))
                q.append((r,c+1))
                q.append((r,c-1))

sol = Solution()
m= [["X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],["O","X","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","X","X"],["O","O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","X"],["O","O","X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","X","O"],["O","O","O","O","O","X","O","O","O","O","X","O","O","O","O","O","X","O","O","X"],["X","O","O","O","X","O","O","O","O","O","X","O","X","O","X","O","X","O","X","O"],["O","O","O","O","X","O","O","X","O","O","O","O","O","X","O","O","X","O","O","O"],["X","O","O","O","X","X","X","O","X","O","O","O","O","X","X","O","X","O","O","O"],["O","O","O","O","O","X","X","X","X","O","O","O","O","X","O","O","X","O","O","O"],["X","O","O","O","O","X","O","O","O","O","O","O","X","X","O","O","X","O","O","X"],["O","O","O","O","O","O","O","O","O","O","X","O","O","X","O","O","O","X","O","X"],["O","O","O","O","X","O","X","O","O","X","X","O","O","O","O","O","X","O","O","O"],["X","X","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","O"],["O","X","O","X","O","O","O","X","O","X","O","O","O","X","O","X","O","X","O","O"],["O","O","X","O","O","O","O","O","O","O","X","O","O","O","O","O","X","O","X","O"],["X","X","O","O","O","O","O","O","O","O","X","O","X","X","O","O","O","X","O","O"],["O","O","X","O","O","O","O","O","O","O","X","O","O","X","O","X","O","X","O","O"],["O","O","O","X","O","O","O","O","O","X","X","X","O","O","X","O","O","O","X","O"],["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],["X","O","O","O","O","X","O","O","O","X","X","O","O","X","O","X","O","X","O","O"]]
sol.solve(m)
print (m)
