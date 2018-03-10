class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int

        Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray
        of which the sum ≥ s. If there isn't one, return 0 instead.

        [2,5,6,8,12,15]
        For example, given the array [2,3,1,2,4,3] and s = 7, return 2, because the subarray [4,3] has the minimal length
        (2) under the problem constraint

        Keep 2 points: left and i.
        Start by keeping left at first index, then move i to the right and adding each number to sum.
        As soon as sum becomes >=s, update min distance between left and i, then move left pointer to the right by one,
        and subtract whatever number was passed over by the left pointer from the sum, keeping doing this until sum is
        no longer >= s.

        Then continue by moving i to the right and adding sum again like above.

        """
        left, sum, min_size = 0, 0, float('inf')
        for i, n in enumerate(nums):
            sum += n
            while (sum >= s and left <= i): #If sum has reached or surpassed s and left is still behind 'i'
                min_size = min(min_size, i-left+1) #update min size
                sum -= nums[left] #update sum to remove whatever was passed over by left.
                left += 1 #Move left to the right by 1 to start a new 'window' and see if it can be smaller.

        return min_size if min_size < float('inf') else 0

sol = Solution()
print (sol.minSubArrayLen(7,[2,3,1,2,4,3]))
