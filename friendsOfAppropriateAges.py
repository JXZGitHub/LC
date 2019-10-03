import collections


class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int

        Time: O(max(len(ages),121))
        Space: O(1) #Constant 121

        """
        numInAges = collections.defaultdict(int)
        sumInAges = collections.defaultdict(int)
        res = 0
        for a in ages:
            numInAges[a] += 1
        for i in range(1, 121):  # Max age in the list is 120
            sumInAges[i] = numInAges[i] + sumInAges[i - 1]
        for i in range(1, 121):
            if numInAges[i] == 0:
                continue
            count = sumInAges[i] - sumInAges[i // 2 + 7]
            res += max(0, count * numInAges[i] - numInAges[i])
            # Why max()?
            # If you don't use max(), you must start with i in range(15,l21),
            # 15 because B has to be both >A*0.5+7 and <= A, so B falls into ( A*0.5+7,A ]
            # which means we must satisfy A*0.5+7 < A, so A >= 15. So there's no way to get any friends for ages < 15.
        return res

sol = Solution()
print (sol.numFriendRequests([5,24,82]))