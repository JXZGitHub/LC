class Solution:
    def subsets_recursive(self, nums):
        """
        O(2^n). Space O(1)
        :type nums: List[int]
        :rtype: List[List[int]]

        Given a set of distinct integers, nums, return all possible subsets (the power set).
        Note: The solution set must not contain duplicate subsets.

        Example:

        Input: nums = [1,2,3]
        Output:
        [
          [3],
          [1],
          [2],
          [1,2,3],
          [1,3],
          [2,3],
          [1,2],
          []
        ]

        """
        # [1,2,3], [ [],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3] ]
        res = []
        self.generateSet(nums, 0, res, [])
        return res

    def generateSet(self, nums, startingPos, res, subRes):
        res.append(subRes[:])
        for i in range(startingPos, len(nums)):
            subRes.append(nums[i])
            self.generateSet(nums, i + 1, res, subRes)
            subRes.pop()

    def subsets_iterative(self, nums):
        """
        O(n*2^n): If there are n numbers in the set, there are 2^n power set (2^n total number of subsets including empty).
        Space O(1)

        :type nums: List[int]
        :rtype: List[List[int]]

        Given a set of distinct integers, nums, return all possible subsets (the power set).
        Note: The solution set must not contain duplicate subsets.

        Example:

        Input: nums = [1,2,3]
        Output:
        [
          [3],
          [1],
          [2],
          [1,2,3],
          [1,3],
          [2,3],
          [1,2],
          []
        ]

        """
        # [1,2,3], [ [],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3] ]
        result = [[]]
        for i in range(len(nums)):
            size = len(result)
            for j in range(size):
                result.append(list(result[j])) #Make a copy of every existing result's element, and append to end.
                result[-1].append(nums[i])     #Then append to that last 'copy' with the latest element of num.
        return result

sol = Solution()
print (sol.subsets_recursive([1,2,3]))
print (sol.subsets_iterative([1,2,3]))