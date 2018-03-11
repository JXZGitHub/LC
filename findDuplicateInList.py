class Solution:
    """
    Given an unsorted array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
    Assume that there is at least one duplicate number, return the duplicate one.
    Note:
    There is only one duplicate number in the array, but it could be repeated more than once.
    """
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                return n

    def findDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for n in nums:
            if n in seen:
                return n
            else:
                seen.add(n)

    def findDuplicate3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        c = Counter(nums)
        return c.most_common(1)[0][0]
