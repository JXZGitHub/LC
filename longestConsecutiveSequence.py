import collections
class Solution_Faster_Clever:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Time: O(N)
        Space: O(N)
        """
        res = 0
        remaining = set(nums)
        for n in nums:
            if n in remaining:  # all n's in a given sequence will be removed from the set in one go.
                remaining.remove(n)
                prevNum, nextNum = n - 1, n + 1
                while prevNum in remaining:
                    remaining.remove(prevNum)
                    prevNum -= 1
                while nextNum in remaining:
                    remaining.remove(nextNum)
                    nextNum += 1
                sequenceLength = nextNum - prevNum - 1
                res = max(res, sequenceLength)
        return res


class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Time: O(N)
        Space: O(N)

        Using Union Find. For each node, try to union its n-1 and n+1.
        And find the max count all root node's members.

        """
        parents = {}
        parentToCount = collections.defaultdict(int)
        for n in nums:
            parent = self.find(n, parents)
            for neighbor in (n - 1, n + 1):
                if neighbor in parents:
                    parentOfNeighbor = self.find(neighbor, parents)
                    if parentOfNeighbor < n:
                        parents[n] = parentOfNeighbor
                    elif parentOfNeighbor > n:
                        parents[neighbor] = parents[n]

        for p in parents:
            parent = self.find(p, parents)
            parentToCount[parent] += 1

        return max(parentToCount.values()) if parentToCount else 0

    def find(self, node, parents):
        if node not in parents:
            parents[node] = node
            return node
        if parents[node] != node:
            parents[node] = self.find(parents[node], parents)
        return parents[node]