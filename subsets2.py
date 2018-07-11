class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Time: O(n*2^n):
              If there are n numbers in the set, there are 2^n items in its power set (2^n total number of subsets including empty).
              Therefore there are 2^n recursive function calls, and within each call it loops through len(nums) times.
              So total runtime is n*2^n.
        Space O(1)

        """
        nums.sort() #sort first, to better remove duplicate durign recursion.
        res = []
        self.recurse(nums, [], res, 0)
        return res

    def recurse(self, nums, output, res, start):
        res.append(output[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]: #remove duplicates.
                continue
            output.append(nums[i])
            self.recurse(nums, output, res, i + 1)
            output.pop()

sol = Solution()
print (sol.subsetsWithDup([1,1,2]))
print (sol.subsetsWithDup([1,2,3]))