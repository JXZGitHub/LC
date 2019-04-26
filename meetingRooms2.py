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

    def minMeetingRooms_no_heap(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        Time: O(n Logn)
        Space: O(2n)
        """
        start, end = [], []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)

        start.sort()
        end.sort()

        s,e=0,0
        room_in_use = 0
        min_room_used = 0
        while s<len(start):
            if start[s] < end[e]:
                room_in_use += 1
                min_room_used = max(min_room_used,room_in_use)
                s+=1
            else:
                room_in_use -=1
                e+=1
        return min_room_used




sol = Solution()
print (sol.minMeetingRooms([Interval(0,30),Interval(5,10),Interval(15,20)]))