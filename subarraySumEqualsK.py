import collections
class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Time: O(N)
        Space: O(N)

        Iterate through array, keep track of each cumulative sum and how many times it occured.

        If the latest cumulative sum is S, and there already exists previous cumulative sum of S-k,
        then there must be X ways to add to S, where X is the number of occurences of S-k seen before.
        """
        cumSum_to_freq = collections.defaultdict(
            int)  # Number of occurences of a given cumulative (continuous subarray) sum
        cumSum_to_freq[0] = 1  # Any subarray that adds to K will automatically count towards AT LEAST one result.
        cumSum = 0
        res = 0
        for n in nums:
            cumSum += n
            res += cumSum_to_freq[cumSum - k]
            cumSum_to_freq[cumSum] += 1
        return res

    def subarraySum_return_all_subarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Time: O(N)
        Space: O(N)

        This is a followup: return all such subarrays.
        Same idea, except we keep track of all ending indices of prev cumulative sum.
        And at a given index i, and S-k exists, then the subaray must starting RIGHT AFTER the index of S-k,
        and ending AT i.
        """
        cumSum_to_index = collections.defaultdict(list)  # All ending indices of a given cumulative (continuous subarray) sum
        cumSum_to_index[0] = [-1]  # Starting from 0 for given cumulative sum that adds to exactly k.
        cumSum = 0
        resIndices = []
        res = []
        for i, n in enumerate(nums):
            cumSum += n
            for c in cumSum_to_index[cumSum - k]:
                resIndices.append((c + 1, i))  # why c+1: any subarray that adds to K will automatically start from +1
                                               # of its S-K's index.
            cumSum_to_index[cumSum].append(i)

        for start, end in resIndices:
            res.append(nums[start:end + 1])

        return res
