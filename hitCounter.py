from collections import deque

class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.q.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        count = 0
        for t in reversed(self.q):
            if timestamp - t < 300:
                count += 1
        return count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

class HitCounterScalable(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque

        self.num_of_hits = 0
        self.time_hits = deque()


    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if not self.time_hits or self.time_hits[-1][0] != timestamp:
            self.time_hits.append([timestamp, 1])
        else:
            self.time_hits[-1][1] += 1 #If multiple arrivals in same timestamp, dont add more to the queue, just increment existing.

        self.num_of_hits += 1


    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.time_hits and timestamp - self.time_hits[0][0] >= 300:
            #Remove from queue anything beyong last 300 seconds, and update number_of_hits
            self.num_of_hits -= self.time_hits.popleft()[1]

        return self.num_of_hits