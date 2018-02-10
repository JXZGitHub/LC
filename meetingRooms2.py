import heapq


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda x: x.start)
        rooms = [] #Number of rooms needed
        for meeting in intervals:
            if rooms and meeting.start >= rooms[0]: #If a meeting starts AFTER the meeting end time of the shortest duration's room, then share that same room.
                heapq.heapreplace(rooms, meeting.end)
            else: #otherwise, if no room reserved at all or meeting starts BEFORE even the shortest duration end time's room, need a new room
                heapq.heappush(rooms, meeting.end)
        return len(rooms)

