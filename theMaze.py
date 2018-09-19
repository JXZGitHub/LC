class Solution:
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        visited = set()
        return self.traverse(maze, visited, tuple(start), destination)

    def traverse(self, maze, visited, location, destination):
        if location in visited:
            return
        if list(location) == destination:
            return True
        visited.add(location)
        x, y = location[0], location[1]
        directions = []
        while y - 1 >= 0 and maze[x][y - 1] != 1:
            y -= 1
        if y != location[1]:
            directions.append((x, y))

        x, y = location[0], location[1]
        while y + 1 <= len(maze[0]) - 1 and maze[x][y + 1] != 1:
            y += 1
        if y != location[1]:
            directions.append((x, y))

        x, y = location[0], location[1]
        while x + 1 <= len(maze) - 1 and maze[x + 1][y] != 1:
            x += 1
        if x != location[0]:
            directions.append((x, y))

        x, y = location[0], location[1]
        while x - 1 >= 0 and maze[x - 1][y] != 1:
            x -= 1
        if x != location[0]:
            directions.append((x, y))

        for d in directions:
            if self.traverse(maze, visited, d, destination):
                return True
        return False
