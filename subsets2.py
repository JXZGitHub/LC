class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Time: O(n*2^n):
              If there are n numbers in the set, there are 2^n items in its power set (2^n total number of subsets including empty).
              Therefore there are 2^n recursive function calls, and within each call it loops through len(nums) times.
              So total runtime is n*2^n.
        Space O(n)

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

class Solution_Iterative(object):
    def subsetsWithDup(self, nums):
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
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: #Dup found.
                startingIndex = size #Previous result size, starting there to skip those sets that don't need the duplicate.
            else:
                startingIndex = 0
            size = len(result) #Current result size.
            for j in range(startingIndex, size):
                result.append(list(result[j])) #Make a copy of every existing result's element, and append to end.
                result[-1].append(nums[i])     #Then append to EVERY 'copy' with the latest element of num.
        return result

sol = Solution()
sol2 = Solution_Iterative()
print (sol.subsetsWithDup([1,1,2]))
print (sol2.subsetsWithDup([1,1,2]))