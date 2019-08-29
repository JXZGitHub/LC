import heapq
import collections


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int

        Time: O(n) #heappush is log(len(tasks)), but there can be maximum of 26 (letters in alphabet) tasks. So it's log(26) a constant.
        Space: O(len(tasks)) ==> O(1), at most 26 so constant again.
        """
        cycles = n + 1
        task_counter = collections.Counter(tasks)  # len(task_counter) is number of differnet tasks.
        res = 0
        q = []
        for count in task_counter.values():
            heapq.heappush(q, -count)

        while q:  # If there are tasks remaining
            tasks_executed = 0
            tasks_counts = []
            for _ in range(cycles):
                if q: #if q has less than cycles of jobs left, then there might be padding with idle cycles.
                    tasks_counts.append(-heapq.heappop(q))
                    tasks_executed += 1

            # At this point, tasks_executed is <= cycles.
            for count in tasks_counts:
                count -= 1
                if count:
                    heapq.heappush(q, -count)  # if there are still remaining count of this task, put back to q.

            if q:  # If still remaiing tasks to be executed, then the most recent cycle was fully populated (either with all tasks or some idles):
                res += cycles
            else:
                res += tasks_executed  # Else, whatever remaining tasks (popped from q) can fit int the current cycle fine, and we end here.

        return res

sol = Solution()
print (sol.leastInterval(["A","A","A","B","B","B"],2))
#print (sol.leastInterval(["A","A","A","B","B","B","C","D"],2))