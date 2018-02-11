class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Given a collection of distinct numbers, return all possible permutations.

        For example,
        [1,2,3] have the following permutations:
        [
          [1,2,3],
          [1,3,2],
          [2,1,3],
          [2,3,1],
          [3,1,2],
          [3,2,1]
        ]

        #Recursive Depth First Search.

        """
        result = []
        visited = [False] * len(nums)
        self.permuteRecursive(nums, [], visited, result)
        return result

    def permuteRecursive(self, nums, currNums, visited, result):
        if len(nums) == len(currNums):
            result.append(currNums[:])
            # Since list is mutable, '+[]' is to create a new list that is identical to currNums,
            # so when currNums gets modifed (pop) later, result won't be changed.
            # equivalently: currNums[:] does the same thing.

            return
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = True
                currNums.append(nums[i])
                self.permuteRecursive(nums, currNums, visited, result)
                currNums.pop()  # Remove right-most number from the list to make way for more calls when this function returns from call stack.
                visited[i] = False  # Restore visited to unvisited for new traversals in a new call up the stack.

sol = Solution()
print (sol.permute([1,2,3]))