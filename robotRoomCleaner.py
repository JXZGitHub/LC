# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        dire_map = {
            0: (-1, 0),
            90: (0, 1),
            180: (1, 0),
            270: (0, -1),
        }

        def backTrackHelper(i, j, cur_dir):
            if (i, j) in visited:
                return
            else:
                robot.clean()
                visited.add((i, j))
                for _ in range(4):
                    if robot.move():
                        dx, dy = dire_map[cur_dir]
                        backTrackHelper(i + dx, j + dy, cur_dir)

                        # Return to its previous cell once the last backtracking call returns
                        # (it visited a previous cell)
                        robot.turnLeft()
                        robot.turnLeft()
                        robot.move()
                        robot.turnRight()  # These 2 turnRight restores the original direction.
                        robot.turnRight()

                    # Move onto the next direction to try. Remember, since the loop goes around 4 times,
                    # it'll cycle through 4 directions to COME BACK to the orignal direciotn AT which the backtracking call is initialized.
                    robot.turnRight()
                    cur_dir += 90
                    cur_dir %= 360

        backTrackHelper(0, 0, 0)
