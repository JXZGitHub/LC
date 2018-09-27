class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str

        Time: O(1)  #Number of input is constant.
        Space: O(1)
        """

        st = set([time[0], time[1], time[3], time[4]])
        s = ''.join(sorted(list(st)))
        newTime = time
        for i in range(len(time) - 1, -1, -1):
            size = len(s) - 1
            if i == 2:
                continue
            digit = time[i]
            s_index = s.find(digit)
            if s_index == size:
                newTime = newTime[:i] + s[0] + newTime[i + 1:]
                continue
            nextNumber = s[s_index + 1]
            if i == 4:
                return newTime[:i] + nextNumber + newTime[i + 1:]
            elif i == 3:
                if int(nextNumber) < 6:
                    return newTime[:i] + nextNumber + newTime[i + 1:]
            elif i == 1:
                if int(newTime[0]) < 2 or int(nextNumber) <= 3:
                    return newTime[:i] + nextNumber + newTime[i + 1:]
            else:
                if int(nextNumber) <= 2:
                    return newTime[:i] + nextNumber + newTime[i + 1:]
            newTime = newTime[:i] + s[0] + newTime[i + 1:]

        return newTime


class Solution_try_all_possibilities:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        Time: O(1)  #Number of input is constant.
        Space: O(1)
        """

        totalMins = 60 * 24
        s = set(time)
        currentMin = int(time[:2]) * 60 + int(time[3:])
        for i in range(1, totalMins + 1):
            timeToTry = (currentMin + i) % totalMins
            hh, mm = divmod(timeToTry, 60)
            time = '{:02d}'.format(hh) + ':' + '{:02d}'.format(mm)
            if set(time) <= s:
                return time
        return None