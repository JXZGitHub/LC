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
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if nums[low] == nums[high]:
                low -=1
                continue
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
sol = Solution()
print (sol.search([3, 1, 2, 3, 3, 3, 3],1))

