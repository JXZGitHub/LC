class Solution(object):
    def reverseWords2(self, s):
        words = s.split()
        return ' '.join(words[::-1]).strip()

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        rightIndex = leftIndex = len(s)-1
        reverseString = ''
        while leftIndex >= 0:
            if s[leftIndex]==' ':
                numOfSpaces = self.countSpaces(s,leftIndex)
                if s[rightIndex]!=' ':
                    reverseString += (s[leftIndex+1:rightIndex+1]+' ')
                leftIndex -= numOfSpaces
                rightIndex = leftIndex
            else:
                leftIndex -= 1

        reverseString += (s[leftIndex+1:rightIndex + 1])

        if reverseString and reverseString[0]== ' ':
            reverseString = reverseString[1:]
        if reverseString and reverseString[-1] == ' ':
            reverseString = reverseString[:-1]
        return reverseString

    def countSpaces(self, s, index):
        count = 0
        i = -(len(s)-index)
        for c in s[i::-1]:
            if c != ' ':
                break
            else:
                count +=1
        return count

s=Solution()
print ('*' + s.reverseWords(' This is  ')+'*')
print ('*' + s.reverseWords('This is   big')+'*')
print ('*'+s.reverseWords('This is big')+'*')
print ('*'+s.reverseWords('Thisisbig')+'*')
print ('*'+s.reverseWords('This   ')+'*')
print ('*'+s.reverseWords('This ')+'*')
print ('*'+s.reverseWords('  This')+'*')
print ('*'+s.reverseWords(' This')+'*')
print ('*'+s.reverseWords('This')+'*')
print ('*'+s.reverseWords('')+'*')
print ('*'+s.reverseWords(' ')+'*')
print ('*'+s.reverseWords('  ')+'*')

