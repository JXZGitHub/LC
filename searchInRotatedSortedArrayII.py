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
            return False

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high-low) // 2
            if target == nums[mid]:
                return True
            if nums[low] == nums[high]:
                #Duplicate number in input:  123333 -> rotates around the last 3 to be: 312333.
                #in this case the start and ending numbers are the same.
                #So we keep advancing until we gets rid of the low.
              #  low +=1
              #  continue
                pass
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
        return False

sol = Solution()
print (sol.search([3, 1, 2, 3, 3, 3, 3],1))