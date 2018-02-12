class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        #Recursive Depth First Search.

        Time O(N*N!). Space O(N)
        """
        result = []
        visited = [False for _ in range(len(nums))]
        self.permuteRecursive(nums, [], visited, result)
        return result

    def permuteRecursive(self, nums, currNums, visited, result):
        if len(nums) == len(currNums):
            result.append(currNums[:])
            return
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = True
                currNums.append(nums[i])
                self.permuteRecursive(nums, currNums, visited, result)
                currNums.pop()  # Remove right-most number from the list to make way for more calls when this function returns from call stack.
                visited[i] = False  # Restore visited to unvisited for new traversals in a new call up the stack.

