import heapq
from collections import Counter

class Solution:
    """
    Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters
    represent different tasks.Tasks could be done without original order.
    Each task could be done in one interval.
    For each interval, CPU could finish one task or just be idle. However, there is a non-negative cooling interval n
    that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or
    just be idle.

    You need to return the least number of intervals the CPU will take to finish all the given tasks.
    Example 1:
    Input: tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8
    Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

    Finish highest frequency tasks first, by diversifying the tasks as much as possible.

    Time: L+L*logL+L*(n+n*L*LogL) ?????
    Space: O(L), where L is length of tasks

    """
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        taskCount = Counter(tasks)
        q = [-1 * v for v in taskCount.values()]
        heapq.heapify(q)
        cycle = n + 1
        res = 0
        while q:
            temp = []
            count = 0
            for _ in range(cycle):
                if q:
                    temp.append(-1 * heapq.heappop(q))
                    count += 1
            for t in temp:
                t -= 1
                if t > 0:
                    heapq.heappush(q, -1 * t)

            if q:
                res += cycle
            else:
                res += count
        return res

sol = Solution()
print (sol.leastInterval(["A","A","A","B","B","B"],2))
print (sol.leastInterval(["A","A","A","B","B","B","C","D"],2))