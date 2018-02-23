class Solution:
    """

    Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

    Example:
    Given nums = [1,1,2]

    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
    It doesn't matter what you leave beyond the new length.

    """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        end = len(nums)
        while i < end:
            if i > 0 and nums[i] == nums[i - 1]:
                start = i
                while (start < end - 1):
                    nums[start] = nums[start + 1]
                    start += 1
                end -= 1
            else:
                i += 1

        return end

    def removeDuplicates_twopointer(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Two pointers, one is faster than the other by 1. If faster one is different from slower one, move both faster and slow up by 1.
        else, keep moving faster until it's different from slower again, then replace slow+1 with the faster one, then move faster again.
        """
        if not nums:
            return 0
        pre = 0
        curr = 0
        while curr < len(nums):
            if nums[curr] != nums[pre]:
                pre += 1
                nums[pre] = nums[curr]
            curr += 1

        return pre + 1

sol = Solution()
nums = [1,1,1,1,1,2,3,4,4,5,5,5]
print (nums[:sol.removeDuplicates_twopointer(nums)])