class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        All numbers (including target) will be positive integers.
        The solution set must not contain duplicate combinations.
        Example 1:

        Input: candidates = [2,3,6,7], target = 7,
        A solution set is:
        [
        [7],
        [2,2,3]
        ]
        Example 2:

        Input: candidates = [2,3,5], target = 8,
        A solution set is:
        [
        [2,2,2,2],
        [2,3,3],
        [3,5]
        ]

        Time: O(k * n^k), k is worst length of a combination, and n is length of candidates.
        Space: O(k): at most k calls on the stack before back tracking.
        """
        res = []
        combo = []
        candidates.sort()
        self.recurse(candidates, 0, target, combo, res)
        return res

    def recurse(self, candidates, start, target, combo, res):
        if target == 0:
            res.append(combo[:])
        else:
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    return
                combo.append(candidates[i])
                self.recurse(candidates, i, target - candidates[i], combo, res)
                combo.pop()

sol = Solution()
print (sol.combinationSum([3,2,5],8))