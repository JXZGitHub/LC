import heapq
from random import choice

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        negativeNums = list(map(lambda x: -x, nums))
        heapq.heapify(negativeNums)
        for _ in range(k - 1):
            heapq.heappop(negativeNums)
        return -heapq.heappop(negativeNums)



import random
class Solution2:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    # Time: (n*log(n))
    # Space: (n)
    def findKthLargest(self, nums, k):
        if not nums:
            return None
        pivotIndex = len(nums) / 2
        pivot = nums[pivotIndex]
        nums1 = []
        nums2 = []
        for i, n in enumerate(nums):
            if i != pivotIndex and n >= pivot:
                nums1.append(n)
            elif n < pivot:
                nums2.append(n)

        if len(nums1) + 1 > k:
            return self.findKthLargest(nums1, k)
        if len(nums1) + 1 == k:
            return pivot
        else:
            return self.findKthLargest(nums2, k - len(nums1) - 1)


        # sol = Solution()
# print (sol.findKthLargest([1],1))

sol = Solution2()
print (sol.findKthLargest([9,10,2,8,3,5],2))


