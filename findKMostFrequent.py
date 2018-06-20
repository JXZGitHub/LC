import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        word_count = collections.defaultdict(int)
        res = []
        for n in nums:
            word_count[n] += 1
        freq = [[] for _ in range(len(nums) + 1)]
        for n, c in word_count.items():
            freq[c].append(n)
        count = 0
        for i in range(len(freq) - 1, 0, -1):
            while freq[i] and count < k:
                res.append(freq[i].pop())
                count += 1
        return res

    # def topKFrequent(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: List[int]
    #     """
    #     count = collections.Counter(nums)
    #     freqs = [ [] for _ in range(len(nums)+1)]
    #     res = []
    #     n = len(nums)
    #     for num, freq in count.items():
    #         freqs[freq].append(num)
    #     while k:
    #         while not freqs[n]:
    #            n -= 1
    #         res.append(freqs[n].pop())
    #         k -= 1
    #     return res

    def topKFrequent2(self, nums, k):
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
            freqList[cntDict[p]].append(p) #If there's more than 1 num that appeared same number of times, append the numbers
        ans = []
        for p in range(n, 0, -1):
            ans += freqList[p] #same as ans.extend(freqList[p]), so emtpy list [] doens't end up being added to ans.
        return ans[:k]

sol = Solution()
print (sol.topKFrequent([1,1,1,2,2,3],2))
#print (sol.topKFrequent2([1,2,3],2))