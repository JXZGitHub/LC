class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

        Time: O(N)
        Space: O(1)

        Use 'first', 'last' as separation index's: all elements to the left of 'first' are 0's, and all elements to the right of 'last' are 2's. And all elements in the middle are 1's
        """
        first = 0
        last = len(nums) - 1
        i = first
        while i <= last:
            if nums[i] == 1:  # 1 is always in the right position.
                i += 1
            elif nums[i] == 0:  # 0 means it must be moved to the left of 'first'
                nums[i], nums[first] = nums[first], nums[i]
                first += 1  # Keep 0's to the left of first
                i += 1  # We know what's moved here must be a 1 or 0, as a 2 is would've been swapped to the end already. So we move i ahead.
            elif nums[i] == 2:
                nums[i], nums[last] = nums[last], nums[i]
                last -= 1  # Keep 2's to the right of first.
                # We don't want to move i ahead yet, because we don't know whats been swapped from the right.


sol = Solution()
x = [2,0,2,1,1,0]
sol.sortColors(x)
print (x)
