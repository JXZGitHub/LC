class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        res = set()
        for n in nums2:
            if self.binary_search(n, nums1):
                res.add(n)
        return list(res)

    def binary_search(self, n, nums):
        if not nums:
            return False
        target_index = len(nums) // 2
        target = nums[target_index]
        if n == target:
            return True
        elif n > target:
            return self.binary_search(n, nums[target_index + 1:])
        elif n < target:
            return self.binary_search(n, nums[:target_index])

class Solution2(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))
