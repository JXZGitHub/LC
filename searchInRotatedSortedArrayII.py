class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            midV = nums[mid]
            loV = nums[lo]
            hiV = nums[hi]

            if target in (loV, hiV, midV):
                return True

           # if loV == hiV:
             #   lo += 1
           #    continue

            if loV <= midV:  # Mid in first increasing subarray
                if loV < target < midV:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif loV > midV:
                if midV < target < hiV:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False

sol = Solution()
print (sol.search([3, 1, 2, 3, 3, 3, 3],1))