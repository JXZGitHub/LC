class Solution:
    def findDuplicate(self, nums):
        """
        Time: O(n*log(n))
        Space: (1)

        Use mid index (not value) of nums as pivot, count any n that is <= mid index and any n that is > mid index.
        If the count is <= mid index, then duplicate must be in the right hand side, else in the left hand side.

        """
        left,right=0,len(nums)-1
        while left<right:
            mid = left + (right-left)//2
            count = 0
            for n in nums:
                if n <= mid:
                    count +=1
            if count <= mid:
                left = mid + 1
            else:
                right = mid
        return left

    def findDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time: O(N)
        Space: O(1)

        Create a "linked list" where the value of each node is a value in nums, but that value is derived from
        using previous node's value as the index of nums, and finding nums[index].

        The starting node's value is nums[0].
        Then find cycle in the list by moving slow one step, and fast 2 steps until slow == fast.
        Then RESET FAST = 0. And start moving each by one step until they meet again.
        """
        if (len(nums) > 1):
            slow = nums[0]
            fast = nums[nums[0]]

            while (slow != fast):
                slow = nums[slow]
                fast = nums[nums[fast]]

            # Why fast =0 ?  Because once slow and fast meet,
            # it may NOT be the start of the cycle, and the distance from slow to
            # start of cycle is always equal to distance from start of the linked list to the start of cycle.
            # So moving FAST=0 ensures slow and fast are same distance from start of cycle.
            # The proof is left for you to show.
            fast = 0

            while (fast != slow):
                fast = nums[fast]
                slow = nums[slow]
            return slow
        return -1
sol = Solution()
print (sol.findDuplicate([4,4,1,2,3]))
#print (sol.findDuplicate([2,2,2,6,4,5,3]))
