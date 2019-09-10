import heapq

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def minMeetingRooms_heap(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        Time: O(nlogn)
        Space: O(n)
        """
        intervals.sort(key=lambda x: x.start)
        rooms = [] #Number of rooms needed
        for meeting in intervals:
            if rooms and meeting.start >= rooms[0]:
                #If a meeting starts AFTER the meeting end time of the shortest duration's room,
                # then share that same room.
                heapq.heapreplace(rooms, meeting.end)
            else:
                #otherwise, if no room reserved at all or meeting starts BEFORE even the shortest
                #duration end time's room, need a new room
                heapq.heappush(rooms, meeting.end)
        return len(rooms)

    class Solution_no_heap(object):
        def minMeetingRooms(self, intervals):
            """
            :type intervals: List[List[int]]
            :rtype: int
            """
            starts = sorted(i[0] for i in intervals)
            ends = sorted(i[1] for i in intervals)
            e = 0
            i = 0
            rooms = 0
            for s in starts:
                if s >= ends[e]:
                    e += 1
                else:
                    rooms += 1
            return rooms

sol = Solution()
print (sol.minMeetingRooms([Interval(0,30),Interval(5,10),Interval(15,20)]))