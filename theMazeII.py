class Solution:
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int

        BFS:
        Time: O(M*N*max(M,N)) <-- for every node, it needs to travel a max of the longest possible width or height.
        Space: O(M*N)
        """
        maxRow = len(maze)
        maxCol = len(maze[0])
        dp = [[float('inf') for _ in range(maxCol)] for _ in
              range(maxRow)]  # Minimum number of steps to reach dp[i][j] from start location
        dp[start[0]][start[1]] = 0
        q = [(start[0], start[1])]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            newQ = []
            for x, y in q:
                for d in directions:
                    newX, newY = x, y
                    dist = dp[x][y]
                    dx, dy = d[0], d[1]
                    while 0 <= newX < maxRow and 0 <= newY < maxCol and maze[newX][newY] == 0:
                        newX += dx
                        newY += dy
                        dist += 1
                        print (newX, maxRow, newY, maxCol)
                    newX -= dx
                    newY -= dy
                    dist -= 1
                    print(newX, maxRow, newY, maxCol)
                    if dist < dp[newX][newY]:
                        dp[newX][newY] = dist
                        if newX != destination[0] or newY != destination[1]:
                            newQ.append((newX, newY))
            q = newQ

        if dp[destination[0]][destination[1]] != float('inf'):
            return dp[destination[0]][destination[1]]
        else:
            return -1


class Solution_DFS_TOO_SLOW:
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        visited = set()
        distance, shortest = self.traverse(maze, tuple(start), visited, tuple(destination), float('inf'))
        return shortest

    def traverse(self, maze, location, visited, destination, shortest):
        x, y = location[0], location[1]
        maxRow = len(maze) - 1
        maxCol = len(maze[0]) - 1
        if location in visited:
            return -1, shortest
        if location == destination:
            return 0, shortest
        visited.add(location)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for d in directions:
            newX, newY = x, y
            dx, dy = d[0], d[1]
            while 0 <= newX <= maxRow and 0 <= newY <= maxCol and maze[newX][newY] == 0:
                newX += dx
                newY += dy
            newX -= dx
            newY -= dy
            if newX != x or newY != y:
                distance, shortest = self.traverse(maze, (newX, newY), visited, destination, shortest)
                if distance != -1:
                   distance += newX - x
                   shortest = min(shortest, distance)
        return distance,shortest

sol = Solution()
maze=[[0,0],[0,1],[0,1]]
start=[0,1]
destination=[2,0]
print (sol.shortestDistance(maze,start,destination))



