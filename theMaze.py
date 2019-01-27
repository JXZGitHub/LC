class Solution:
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        DFS:

        Time: O(M*N*max(M,N)) <-- for every node, it needs to travel a max of the longest possible width or height.
        Space: O(M*N)
        """
        visited = set()
        return self.recurse(maze, start, set(), destination)

    def recurse(self, maze, start, visited, destination):
        if start == destination:
            return True
        if tuple(start) in visited:
            return
        visited.add(tuple(start))
        r, c = start[0], start[1]
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            newR = r
            newC = c
            while (0 <= newR < len(maze) and 0 <= newC < len(maze[r]) and maze[newR][newC] == 0):
                newR += dr
                newC += dc
            newR -= dr
            newC -= dc
            if self.recurse(maze, [newR, newC], visited, destination):
                return True
        return False
