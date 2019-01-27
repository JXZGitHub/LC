class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]

        Time:  O(n * C(n, k)), where k i worst length of a given combination, n is length of candidates,
               and C(n,k) is n choose k.

               Branch factor = N first level, N-1 second level, N-2 third level, etc...
               Max possible Depth = k (add every number in the list to be k).
               So Number of Recursive calls = N*(N-1)*(N-2)... for k times. This is the same as N Choose k.
               Inside each recursive call is a loop of size n, n-1, n-2, etc
               O(n*C(n,k)).

        Space: O(k)
        """
        res = []
        output = []
        candidates.sort()
        self.recurse(candidates, 0, output, res, target)
        return res

    def recurse(self, candidates, start, output, res, target):
        if target == 0:
            res.append(output[:])
        else:
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicates, to ensure all combinations are unique.
                if candidates[i] > target:
                    return
                output.append(candidates[i])
                self.recurse(candidates, i + 1, output, res, target - candidates[i])
                output.pop()

