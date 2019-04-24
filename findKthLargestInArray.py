import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Time: O(n*log(k)) = O(n)
        Space: O(k) = O(1)

        Maintain a min heap (because we are looking for k'th LARGEST) of size K,
        and selectively push elements in if size of heap is at K.
        """
        heap=[]
        for n in nums:
            if len(heap)<k:
                heapq.heappush(heap,n)
            else:
                least = heap[0] #Least is the current Kth's largest
                if n > least: #But we now got a bigger Kth's largest, so replace that one.
                    heapq.heapreplace(heap,n)
        return heap[0] #min of heap size K is Kth largest.


class Solution2:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Time: O(N) best case, O(N^2) worst case.
        Space: O(1)

        sub-problem: rearrange nums so that all elements > nums[0] is to its LEFT,
        and all <nums[0] to its RIGHT. nums[0] becomes the pivot.
        Then check if position of the pivot (the 'pivot_location')
        is exactly k-1, <k-1, or >k-1, and do the same on a subset of nums accordingly, until position
        of the pivot is exactly k-1, then pivot is Kth' largest.
        """
        while True:
            pivot_location = self.partition(nums, left, right)
            if pivot_location == k - 1:
                return nums[pivot_location]
            elif pivot_location < k - 1:
                left = pivot_location + 1
            else:
                right = pivot_location - 1
        return None

    def partition(self, nums, left, right):
        pivot = nums[left]
        l = left + 1
        r = right
        while l <= r:
            if (nums[l] < pivot < nums[r]):
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            if nums[l] >= pivot:
                l += 1
            if nums[r] <= pivot:
                r -= 1
        nums[left], nums[r] = nums[r], nums[left]
        return r

import random
class Solution3:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    # Time: O(n)
    # Space: O(1) on heap. O(log(n)) on stack.
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


