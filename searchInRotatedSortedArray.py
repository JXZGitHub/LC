class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        The array will always have 2 increasing segments. First segment's every element is larger than 2nd segment.
        Binary Search around a mid point in the whole array, then detremine if target is in the first and 2nd segment.

        Time: O(logN)
        Space: O(1)
        """

        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            # Explict checking if target mtaches the 3 known points
            if target == nums[mid]:
                return mid
            if target == nums[low]:
                return low
            if target == nums[high]:
                return high

            if nums[low] <= nums[mid]:  # If mid is in the first increasnig subarray
                # Regular binary search
                if nums[low] < target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[low] >= nums[mid]:  # If mid is in the 2nd increasing subarray (ie, every element in 2nd subarray is < than first subarray)
                # Regular binary search
                if nums[mid] < target < nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
sol = Solution()
print (sol.search([4,5,6,7,0,1,2],3))

