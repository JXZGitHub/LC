from collections import deque
class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int

        DIFFERENT from Number of Islands!!

        BFS, finding number of connected components in a undirected graph:

        len(M) can be viewed as number of friends (number of rows of the grid)
        Each M[i][j] can be seen as whether i and j is a friend (connected nodes in a un-directed graph), from the
        perspective of i (row).

        Then we start with the first person (row 0 of M), and then do BFS of all of his friends (any 1's in the same col
        that's not 'visited'), and increment a count whenever the queue is empty (exhausted all connected friends)

        Time: (N^2, where N is the number of friends)
        Space: (N)
        """
        visited = [False for i in range(len(M))]
        q = deque()
        count = 0
        for friend in range(len(M)):  # Go through each in the friend list (total of len(M) friends)
            if not visited[friend]:
                q.append(friend)  # Initial node in the BFS search
                while q:
                    friendA = q.popleft()
                    visited[friendA] = True
                    for friendB in range(len(M)):  # Try to see if friendA is friends with anyone else
                        if not visited[friendB] and M[friendA][friendB] == 1:
                            q.append(friendB)  # Insert friendB as new node in the queue to continue current iteration of BFS

                count += 1  # If a given BFS search ends, we've completed a friend circle. Now let the outer for loop go to the next person in the firend list (if still any unvisited ones left).
        return count

sol = Solution()
print (sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))