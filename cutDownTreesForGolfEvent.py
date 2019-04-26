class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int

        Time: O( (M*N)^2)
        Space; O(M*N)

        Sort the trees in forest by their height, saving the coordinates of each tree.
        Then starting at 0,0 in the forest, find the min steps to reach each tree's coordinates starting with lowest height.
        and keep adding those steps until all trees are processed
        """
        trees = []
        steps = 0
        for r in range(len(forest)):
            for c in range(len(forest[r])):
                if forest[r][c] > 1:
                    trees.append((forest[r][c], r, c))
        trees.sort()
        curr_r, curr_c = 0, 0
        for _, r, c in trees:
            minSteps = self.bfs(forest, curr_r, curr_c, r, c)
            if minSteps == -1:
                return minSteps
            else:
                steps += minSteps
                forest[r][c] = 1
            curr_r, curr_c = r, c
        return steps

    def bfs(self, forest, curr_r, curr_c, r, c):
        if (curr_r, curr_c) == (r, c):
            return 0
        q = [(curr_r, curr_c)]
        visited = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        steps = 0
        while q:
            steps += 1
            new_q = []
            for loc_r, loc_c in q:
                for dr, dc in dirs:
                    new_r, new_c = loc_r + dr, loc_c + dc
                    if (0 <= new_r < len(forest) and 0 <= new_c < len(forest[0]) and (new_r, new_c) not in visited and
                            forest[new_r][new_c] != 0):
                        if (new_r, new_c) == (r, c):
                            return steps
                        visited.add((new_r, new_c))
                        new_q.append((new_r, new_c))
            q = new_q
        return -1


sol = Solution()
print (sol.cutOffTree([[1,2,3],[0,0,0],[7,6,5]]))



