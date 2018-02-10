#s1 = "How about today and today is a nice day"
#s2 = "How and today nice"
#Return words in s1 that are not in s2
def missingWords(s1,s2):
    words1 = s1.split()
    words2 = s2.split()
    print (set(words1).difference(set(words2)))

def missingWords2(s1,s2):
    words1 = s1.split()
    words2 = s2.split()
    words1.sort()
    words2.sort()
    i1 = i2 = 0
    missing = []
    while i1<len(words1) and i2<len(words2):
        if words1[i1] < words2[i2]:
            missing.append(words1[i1])
            i1 += 1
            while (i1<len(words1) and words1[i1]==words1[i1-1]):
                i1+=1
        elif words1[i1] > words2[i2]:
            i2 += 1
            while (i2<len(words2) and words2[i2]==words2[i2-1]):
                i2+=1
        else:
            i1+=1
            i2+=1

    while i1 < len(words1):
        missing.append(words1[i1])
        i1+=1

    print (missing)

#s1 = "How about today hos zbc zxy"
#s2 = "How about today and today is a nice day"
#s2 = "How and today nice"

s1 =  "abc def def def efg efg hij hij xyz"
s2 = "ab  def def hij klm klm klm"

missingWords(s1,s2)
missingWords2(s1,s2)
