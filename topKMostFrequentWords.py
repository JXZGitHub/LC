import heapq
from functools import total_ordering
import collections

@total_ordering
class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __eq__(self, other):
        return self.count == self.count and self.word == self.word

    def __lt__(self, other):
        # Force comparison of words to be reverse lexicagraphical order so that the heap will give correct lex order after popping
        return self.count < other.count or (self.count == other.count and self.word > other.word)


class Solution_heap:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]

        Time: O(n+n*logk+2n) -> O(nlogk)
        Space: (n)
        """
        wordCount = collections.Counter(words)
        heap = []
        res = []
        for (word, count) in wordCount.items():
            heapq.heappush(heap, Element(count, word))
            if len(heap) > k:
                heapq.heappop(heap)
        while heap:
            res.append(heapq.heappop(heap).word)
        return res[::-1]


class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]

        Time: O(2n+ nlogn) -> O(nlogn)
        Space: (n)

        """
        wordCount = collections.Counter(words)
        freq = [[] for i in range(len(words) + 1)]
        res = []
        for word, count in wordCount.items():
            freq[count].append(word)
        for i in range(len(freq) - 1, 0, -1):
            if freq[i]:
                if k == 0:
                    break
                elif k >= len(freq[i]):
                    res.extend(sorted(freq[i]))
                    k -= len(freq[i])
                else:
                    res.extend(sorted(freq[i])[:k])
                    break
        return res



