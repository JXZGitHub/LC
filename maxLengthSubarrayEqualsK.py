class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Time: O(N)
        Space: O(N)

        As you traverse the list, keep a hashmap of the cumulative sum at each index i: {sum:i}.
        Keep adding each number as you traverse, if the current sum = k, then set max length at that index +1 (must be longer than a previous subarray whose sum was k), if current sum is not k, see if there's was index whose cumulative sum was current sum - k using the hashmap. If there is, we know that at index a, sum was (current sum - k), and at index i, sum is current sum, so all the numbers between a+1 and i will add up to k, thus a new subarray length (index i-index a) may be longer than whatever previous max length is.
        """
        subSumToIndex = {}
        currSum = 0
        maxLength = 0
        for i, n in enumerate(nums):
            currSum += n
            if currSum == k:
                maxLength = i + 1
            else:
                subSum = currSum - k
                if subSum in subSumToIndex:
                    maxLength = max(maxLength, i - subSumToIndex[subSum])
            if currSum not in subSumToIndex:
                subSumToIndex[currSum] = i
        return maxLength

    def maxSubArrayContent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Time: O(N)
        Space: O(N)

        As you traverse the list, keep a hashmap of the cumulative sum at each index i: {sum:i}.
        Keep adding each number as you traverse, if the current sum = k, then set max length at that index +1 (must be longer than a previous subarray whose sum was k), if current sum is not k, see if there's was index whose cumulative sum was current sum - k using the hashmap. If there is, we know that at index a, sum was (current sum - k), and at index i, sum is current sum, so all the numbers between a+1 and i will add up to k, thus a new subarray length (index i-index a) may be longer than whatever previous max length is.
        """
        subSumToIndex = {}
        currSum = 0
        maxLength = 0
        start = end = -1
        for i, n in enumerate(nums):
            currSum += n
            if currSum == k:
                maxLength = i + 1
                start,end = 0, i
            else:
                subSum = currSum - k
                if subSum in subSumToIndex and i - subSumToIndex[subSum] > maxLength:
                        start,end = subSumToIndex[subSum] + 1, i
                        maxLength =  i - subSumToIndex[subSum]
            if currSum not in subSumToIndex: # Keep any earlier index to maintain longest size.
                subSumToIndex[currSum] = i
        return nums[start:end+1]


sol = Solution()
print(sol.maxSubArrayLen([-2, -1, 2, 1],1))
print(sol.maxSubArrayContent([-2, -1, 2, 1],1))
print(sol.maxSubArrayLen([1, -1, 5, -2, 3],3))
print(sol.maxSubArrayContent([1, -1, 5, -2, 3],3))