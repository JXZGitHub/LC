class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        #Recursive Depth First Search. Backtracking

        Time: O(N*N!), N is length of nums.
        There are N! calls to self.recurse(), and inside each call, we have to loop through nums (N times)

        Space: O(N)
        """
        res, output, currentIndices = [], [], {}
        nums.sort()
        self.recurse(nums, currentIndices, 0, output, res)
        return res

    def recurse(self, nums, currentIndices, length, output, res):
        if length == len(nums):
            res.append(output[:])
        else:
            for i in range(0, len(nums)):
                if currentIndices.get(i) or \
                  (i > 0 and nums[i - 1] == nums[i] and not currentIndices.get(i - 1)):
                    #Avoid duplicate permutations by
                    #pruning any duplicate that are not already in a permutation 'in progress')
                    continue
                currentIndices[i] = True
                output.append(nums[i])
                self.recurse(nums, currentIndices, length + 1, output, res)
                currentIndices[i] = False
                output.pop()


sol = Solution()
print (sol.permuteUnique([1,1,1,2]))