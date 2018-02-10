#All substring with length num, and distinct num-1 characters
def subStringsLessKDist(inputString, num):
    # WRITE YOUR CODE HERE
    start = 0
    allMatchingSubStrings = []
    for end, c in enumerate(inputString):
        subString = inputString[start:end + 1]
        if (end - start + 1) == num:
            if isMatchingSubstring(subString, num):
                allMatchingSubStrings.append(subString)
            start += 1
    return list(set(allMatchingSubStrings)) #Don't include repeated substrings!!!


def isMatchingSubstring(subString, num):
    uniqueChars = set(subString)
    return len(uniqueChars) == num - 1

print (subStringsLessKDist('democracy',0))
print (subStringsLessKDist('democracydemocracy',5))
print (subStringsLessKDist('ddaabb',3))
print (subStringsLessKDist('awagl awagl',5))
print (subStringsLessKDist('aaaabbc',4))
print (subStringsLessKDist('',100))

# Lengths of Minimum subs sequences without overlaps.
def lengthEachScene(inputList):
    # WRITE YOUR CODE HERE
    charsSeen = set()
    start = 0
    allSequenceLengths = []
    for end, c in enumerate(inputList):
        seq1 = inputList[start:end + 1]
        seq2 = inputList[end + 1:]
        if not hasRepeatingScene(seq1, seq2):
            allSequenceLengths.append(end - start + 1)
            start = end + 1
    return allSequenceLengths


def hasRepeatingScene(seq1, seq2):
    return set(seq1).intersection(seq2)  # intersection means at least one repeat

#print (lengthEachScene(['a','b','c','d','a','e','f','g','h','i','j','e']))
