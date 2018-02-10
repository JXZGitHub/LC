import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        cntDict = collections.defaultdict(int)
        for i in nums:
            cntDict[i] += 1
        freqList = [[] for i in range(n + 1)] #Each sublist is the list of nums that occured X number of times, where X is the index position the sublist in the outer list
        for p in cntDict:
            freqList[cntDict[p]] += p #If there's more than 1 num that appeared same number of times, append the numbers
        ans = []
        for p in range(n, 0, -1):
            ans += freqList[p]
        return ans[:k]

sol = Solution()
print (sol.topKFrequent([1,1,1,2,2,3],2))