class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        The array will always have 2 increasing segments. First segment's every element is larger than 2nd segment.
        Binary Search around a mid point in the whole array, then detremine if target is in the first and 2nd segment.

        Time: O(logN); Worst case O(N) (eg: 311111111)
        Space: O(1)
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[end]:  # Middle point is in the first increasing segment
                if  nums[mid] > target >= nums[start]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] < nums[end]:
                if nums[end] <= target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                end -= 1 #If mid number is EQUAl to the right most number, then the mid number may belong to either the
                # first segment or 2nd. So instead of figuring out which one, we just 'remove duplicate' and move
                # the right pointer left to skip the right most number. And if there's still duplicate,
                # keep doing it in the next loop.
        return False