class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        Change CHARS IN-PLACE, compressed. Return just the updated size of char.
        Input:
        ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

        Output:
        Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
        Explanation:
        Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
        Notice each digit has it's own entry in the array.
        """
        totalIndex, index = 0, 0
        while index < len(chars):
            # For every char, go through the string and check how many repeats there are.
            currChar = chars[index]
            count = 0
            while (index<len(chars) and chars[index] == currChar):
                count +=1
                index +=1

            #Start overriding original char. The overridden version will always be shorter
            # (behind) the original, so won't ever override legitimate characters in the original.
            chars[totalIndex] = currChar
            totalIndex += 1

            if count != 1: #If there's exactly one repeat, override the subsequent repeats with a stringify'ed count.
                for c in str(count):
                    chars[totalIndex] = c
                    totalIndex +=1

        chars[:] = chars[:totalIndex]
        #Discard any remaining chars in the original, as those have already been compressed into the last unique character.
        return len(chars)

sol = Solution()
s=["a","a","a","b","b","a","a"]
sol.compress(s)
s=["a"]
sol.compress(s)
print (s)
s=[]
sol.compress(s)
print (s)
s=["a","b","c"]
sol.compress(s)
print (s)
s=["a","b","b","b","a","a","c","c","c"]
sol.compress(s)
print (s)
