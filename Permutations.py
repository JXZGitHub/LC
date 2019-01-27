class Solution2:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited = [False for _ in range(len(nums))]
        res = []
        nums.sort()
        self.recurse(visited, nums, [], res)
        return res

    def recurse(self, visited, nums, output, res):
        if len(output) == len(nums):
            res.append(output[:])
        else:
            for i in range(len(nums)):
                if not visited[i] and (i == 0 or nums[i] != nums[i - 1]):
                    visited[i] = True
                    output.append(nums[i])
                    self.recurse(visited, nums, output, res)
                    output.pop()
                    visited[i] = False
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited = {}
        res = []
        self.recurse(visited, nums, [], res)
        return res

    def recurse(self, visited, nums, output, res):
        if len(output) == len(nums):
            res.append(output[:])
        else:
            for i in range(len(nums)):
                if not visited.get(nums[i], False):
                    visited[nums[i]] = True
                    output.append(nums[i])
                    self.recurse(visited, nums, output, res)
                    output.pop()
                    visited[nums[i]] = False

sol = Solution2()
print (sol.permute([1,1,2]))