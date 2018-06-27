class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        totalLength = len(nums1) + len(nums2)
        # 1 2 3 4 5 6
        # Pretend that these 2 arrays are merged, then median is given by average of the values at (totalLength + 1) //2
        # and (totalLength+2)//2 positions.
        return (self.findKth(nums1, nums2, (totalLength + 1) // 2) +
                self.findKth(nums1, nums2, (totalLength + 2) // 2)) / 2.0

    def findKth(self, nums1, nums2, k):
        # Finds the kth largest number amongst lists nums1 and nums2 ( both are sorted ) by using binary search.
        if len(nums1) > len(nums2):
            return self.findKth(nums2, nums1, k)  # Force first array to be less than 2nd one, to simply checking if one of them is empty.
        if len(nums1) == 0:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])

        #Starts binary search by looking at the value at half way of K at each array (unless the array is less than k//2, then just end of array) , then if one of those is bigger in one array than the other, eliminate any numbers BEFORE and INCLUDING the smaller value in one of the array, the search for the remaining (k-i or k-jth number), and continue until one of the arrays is empty (conditions above.)
        i, j = min(len(nums1), k // 2), min(len(nums2), k // 2)
        if nums1[i - 1] > nums2[j - 1]:
            return self.findKth(nums1, nums2[j:], k - j)
        else:
            return self.findKth(nums1[i:], nums2, k - i)

