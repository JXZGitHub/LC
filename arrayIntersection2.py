from collections import Counter
from collections import defaultdict

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        return list((c1&c2).elements())

class Solution2(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        Dictionary solution. Time O(M+N). Space O(min(M,N))
        """

        seen = defaultdict(int)
        res = []
        for n in nums1:
            seen[n] += 1
        for n in nums2:
            if seen[n] > 0:
                res.append(n)
                seen[n] -= 1
        return res


class Solution3(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        2 pointer solution. Time O(max(M,N) * max(logM, logN)). Space O(1).
        """
        nums1.sort()
        nums2.sort()
        nums1_i = nums2_i = 0
        res = []
        while nums1_i < len(nums1) and nums2_i < len(nums2):
            if nums1[nums1_i] > nums2[nums2_i]:
                nums2_i += 1
            elif nums1[nums1_i] < nums2[nums2_i]:
                nums1_i += 1
            else:
                res.append(nums1[nums1_i])
                nums1_i += 1
                nums2_i += 1

        return res
