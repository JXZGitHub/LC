class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Binary Serach + DP:
            Maintain DP of size len(nums):
            DP[i] = smallest possible last element of LIS of size i+1.
            DP[0] = minimum of nums.

        Go through the the nums, and start updating or adding to DP: find the 'right boundary' using binary search (first element in DP that's >= nums[i]) and replace dp[i] with the nums[i], or if nums[i] is > than all DPs, append to DP.

        Then, once all DP's are filled, return the length of the DP.

        Time: O(N * log N)
        Space: O(N)
        """
        dp = []
        for n in nums:
            # For each n, use binary search to find the first number >= n, and update that number to be n, which lowers the 'last element of LIS at DP's length', which increase the chance of a longer LIS later on.
            start, end = 0, len(dp) - 1
            index = None
            while start <= end:
                mid = start + (end - start) // 2
                if n >= dp[mid]:
                    start = mid + 1
                elif n < dp[mid]:
                    end = mid - 1
                if dp[mid] == n:
                    index = mid
            if index is None:
                index = start

            # if the right boundary is bigger than all numbers in DP, just add (we've seen a longer LIS)
            if index > len(dp) - 1:
                dp.append(n)
            else:
                # else, lower the last element of the LIS of length index+1 to be n.
                dp[index] = n

        return len(dp)  # Longest we can add to the DP is the longest LIS.


class Solution_slower:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        DP: maintain DP of size len(nums):
        DP[i] = length of longest increasing ending at nums[i].
        DP[0] initialized to 1's ( element has only 1 member)

        To fill each DP[i], go through the all of its previous numbers, and if nums[i] is greater than any of its previous number, DP[i] = max(DP[that prev number index] + 1, DP[i]).

        Then, once all DP's are filled, return the largest value in it.

        Time: O(N^2)
        Space: O(N)
        """
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:  # For a given number, if bigger than any prev number.
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp) if dp else 0


