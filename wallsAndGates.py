from collections import deque
class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.

        You are given a m x n 2D grid initialized with these three possible values.

        -1 - A wall or an obstacle.
        0 - A gate.
        INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
        Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

        For example, given the 2D grid:
        INF  -1  0  INF
        INF INF INF  -1
        INF  -1 INF  -1
          0  -1 INF INF
        After running your function, the 2D grid should be:
          3  -1   0   1
          2   2   1  -1
          1  -1   2  -1
          0  -1   3   4


        Using BFS, start by putting all coordinates of gates (0) into a queue, then find all rooms (inf) at a distance of 1
        from each gate (all directions), and set the value of the room to be 1+the origin's value.
        Then put the coordinates of each room into queue again. This way, all gates and rooms will be visited with
        increasing distances.

        O(m*n), Space (m*n)
        """
        gate = 0
        room = 2147483647
        q = deque()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Put all coordinates of gates into queue
        for row in range(len(rooms)):
            for col in range(len(rooms[row])):
                if rooms[row][col] == gate:
                    q.append((row, col))
        while q:
            row, col = q.popleft()
            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]
                if new_row < 0 or new_col < 0 or new_row >= len(rooms) or new_col >= len(rooms[0]) or rooms[new_row][
                    new_col] != room:
                    continue  # If a neighbor is not a room, skip it.

                rooms[new_row][new_col] = rooms[row][col] + 1  # Otherwise, update the reached room with 1+the value of its origin.
                q.append((new_row, new_col))  # This room needs to be visited again to find all of its neighbors later on.