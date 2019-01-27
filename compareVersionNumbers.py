class Solution:
    def compareVersion_split(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int

        Time: O(N)
        Space: O(1)
        """
        sign = 1
        if len(version1) < len(version2):
            version1, version2 = version2, version1
            sign = -1
        v1 = version1.split('.')
        v2 = version2.split('.')
        i1 = i2 = 0
        while i1 < len(v1) and i2 < len(v2):
            n1 = int(v1[i1])
            n2 = int(v2[i2])
            if n1 > n2:
                return sign * 1
            elif n1 < n2:
                return sign * -1
            i1 += 1
            i2 += 1
        while i1 < len(v1):
            if int(v1[i1]) != 0:
                return sign * 1
            i1 += 1
        return 0

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int

        Time: O(N)
        Space: O(1)
        """
        i1 = i2 = 0
        n1 = n2 = 0
        while i1 < len(version1) or i2 < len(version2):
            while (i1 < len(version1) and version1[i1] != '.'):
                n1 = n1 * 10 + (ord(version1[i1]) - ord('0'))
                i1 += 1
            while (i2 < len(version2) and version2[i2] != '.'):
                n2 = n2 * 10 + (ord(version2[i2]) - ord('0'))
                i2 += 1
            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
            n1 = n2 = 0  # Prepare for comparing the next number between dots.
            i1 += 1
            i2 += 1
        return 0
sol = Solution()
print (sol.compareVersion('1','1.1'))