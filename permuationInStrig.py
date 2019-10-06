import collections
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool

        #Similar to min window substring
        #SLiding window: maintain s1Map of char:count of the target subsring, and neededCbars = len(s1)
        #Go through orignal string, reduce s1Map count for anything in s1Map.
        #If s1Map count >0, then reduced NeededCHars
        #In same loop, while neededChars == 0 (satisfying condition). If i-start+1 = len(s1), then return True.
        # Else, inside while loop, move start of window to the right, and increase s1Map as needed. Increase neededChars if a char's count in s1Map > 0
        """
        s1Map=collections.Counter(s1)
        start=0
        i=0
        charsNeeded = len(s1)
        s1Len = len(s1)
        for i in range(len(s2)):
            c = s2[i]
            if c in s1Map:
                s1Map[c] -= 1
                if s1Map[c] >=0:
                    charsNeeded -= 1
            while charsNeeded == 0:
                if i-start+1 == s1Len:
                    return True
                cStart = s2[start]
                if cStart in s1Map:
                    s1Map[cStart] += 1
                    if s1Map[cStart] >0:
                        charsNeeded += 1
                start+=1
            i++1
        return False
sol = Solution()
print (sol.checkInclusion("ab","eidbaooo"))