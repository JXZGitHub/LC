class Solution(object):
    #Assuming no leading or tradiling spaces, and only ONE space between each word.
    #input 'str' is a list of chars, NOT a str.
    #modify 'str' in place, do not return anything.
    #Reverse each word in str, the reverse whole str.
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        start = 0
        for i in range(len(str)+1): #Loop to length+1 instead of length,
            # so the last index (length; beyond last char) encountered will trigger a reversal of up to last char (index of length-1)
            if i == len(str) or str[i]==' ':
                #If it's the last char, or it's a space, IN-PLACE reverse everything up to the char before this.
                str[start:i] = self.reverseWord(str[start:i])
                start = i + 1
        str = self.reverseWord(str)

    def reverseWord(self, word):
        start = 0
        end = len(word) - 1
        while start < end:
            word[start], word[end] = word[end], word[start]
            start += 1
            end -= 1
        return word

sol = Solution()
s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
sol.reverseWords(s)
print (s)