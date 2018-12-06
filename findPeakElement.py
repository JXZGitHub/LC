class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Assuming: the first element in is peak if its right neighbor is less. last element is peak if its left neighbor
        is less.

        Keep traversing the array until a drop (nums[i] is smaller than nums[i-1]) happens,
        than the peak is right before the drop.
        """
        i = 0
        while i < len(nums):
            if i != 0 and nums[i] < nums[i - 1]:
                break
            i += 1
        return i - 1


class Solution_binary_search:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Assuming: the first element in is peak if its right neighbor is less.
        last element is also peak if its left neighbor is less.

        Pick mid element, if its right neighbor is bigger, then there must be a peak to starting at tis right neighbor.
        if its right neighbor is smaller, then there must be a peak to the left, INCLUDING the mid element.

        Time: O(log(N))
        Space: O(1)
        """
        start, end = 0, len(nums) - 1
        while (start <= end):
            if start == end:
                return start
            mid = start + (end - start) // 2
            if nums[mid + 1] > nums[mid]:
                start = mid + 1
            elif nums[mid + 1] < nums[mid]:
                end = mid #There must be a peak to the left, INCLUDING the mid element, as that could be the peak.

    # While loop will always end because eventaully start will equal to end.
