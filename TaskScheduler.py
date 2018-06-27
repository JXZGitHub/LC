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
    Space: O(1), there can be a maximum length of 26 in the queue, as there are only 26 letters in the alphabet.

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
        cycles = n + 1 # a job + N idle cycles
        res = 0
        while q:
            temp = []
            count = 0
            for _ in range(cycles): #Each iteration in cycle represents a single cpu cycle (ie, a job + N idle cycles )
                if q:
                    temp.append(-1 * heapq.heappop(q)) #Temp stores the remaining number of times each job has.
                    count += 1 #As long as q is not empty, keeps counting until (job + N idle cycles).
                               #else stops counting as there's fewer jobs than cycles left.
            for t in temp:
                t -= 1 #Subtracts once for each job as it was used in the previous loop (picked to be in a cycle)
                if t > 0:
                    heapq.heappush(q, -1 * t) #If there's till more jobs fore ach task, put it back on queue)

            if q:
                res += cycles #If more jobs in queue, it means the full cycle was used, so count it.
            else:
                res += count #else, it means there were fewer jobs than cycle remaining, so just count the number of jobs picked.
        return res

sol = Solution()
print (sol.leastInterval(["A","A","A","B","B","B"],2))
#print (sol.leastInterval(["A","A","A","B","B","B","C","D"],2))