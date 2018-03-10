def binarySearch(start, end, nums, key):
    while (start <= end):
        mid = (end - start) // 2 #Treat mid as offset from start, not absolute index.
        c = nums[start + mid]
        if c == key:
            return start + mid
        elif c > key:
            end = start+mid-1
        else:
            start = start+mid+1
    return None

s=[1,2,3,4,5,6,7]
print (binarySearch(0,len(s)-1,s,5))
s=[1,2,3,4,5]
print (binarySearch(0,len(s)-1,s,5))
s=[1,5,1]
print (binarySearch(0,len(s)-1,s,5))
s=[5]
print (binarySearch(0,len(s)-1,s,5))
s=[5,1]
print (binarySearch(0,len(s)-1,s,5))
s=[1,5]
print (binarySearch(0,len(s)-1,s,5))

s=[1,2,3]
print (binarySearch(0,len(s)-1,s,5))
s=[1]
print (binarySearch(0,len(s)-1,s,5))
s=[]
print (binarySearch(0,len(s)-1,s,5))