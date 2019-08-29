class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]

        Time: O(N*4^N)
        Space: O()
        """
        res = []
        self.recurse(res, num, target, [], 0, 0, 0)
        return res

    def recurse(self, res, num, target, path, startPos, val, lastVal):
        if startPos == len(num):
            if val == target:
                res.append(''.join(path))
        else:
            for i in range(startPos, len(num)):
                if num[startPos] == '0' and i != startPos:
                    break  # prevent number with leading zeroes being used as an item.
                currItem = int(''.join(num[startPos:i + 1]))
                if startPos == 0:
                    path.append(str(currItem))
                    self.recurse(res, num, target, path, i + 1, currItem, currItem)
                    path.pop()
                else:
                    path.append('+')
                    path.append(str(currItem))
                    self.recurse(res, num, target, path, i + 1, val + currItem, currItem)
                    path.pop()
                    path.pop()
                    path.append('-')
                    path.append(str(currItem))
                    self.recurse(res, num, target, path, i + 1, val - currItem, -currItem)
                    path.pop()
                    path.pop()
                    path.append('*')
                    path.append(str(currItem))
                    self.recurse(res, num, target, path, i + 1, val - lastVal + lastVal * currItem, lastVal * currItem)
                    path.pop()
                    path.pop()

