class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        #Recursive Depth First Search. Backtracking

        Time: O(N*N!), N is length of nums.
        There are N! calls to self.recurse(), and inside each call, we have to loop through nums (N times)

        Space: O(N)
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

sol = Solution()
print (sol.permute([1,2,3,4])[4])