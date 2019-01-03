def binarySearch(nums, target):
    """
    Invariant is that the target aleays exists inside [start,end-1] ( same as [start,end), right exclusive )
    Initial condition is therefore: start = 0, end = len(nums)

    If start == end, then there's no element left.
    """
    start,end=0,len(nums)
    while (start < end):
        mid = start + (end - start) // 2 #Treat mid as offset from start, not absolute index.
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid #Don't do mid-1 because end is right exclusive.
        else:
            start = mid+1
    return None

def searchLeftBoundary(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]

    Time O(log N)
    Space: O(1)

    In ascending array, find the position of the last element that's < target OR first element that's = target.
    This is the left boundary
    """
    start, end = 0, len(nums)
    while start < end:
        mid = start + (end - start) // 2
        if target <= nums[mid]:
            end = mid
        elif target > nums[mid]:
            start = mid + 1
    return start


def searchRightBoundary(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]

    Time O(log N)
    Space: O(1)

    In ascending array, find the position of the first element that's > target OR last element that's = target.
    This is the RIGHT boundary.
    """
    start, end = 0, len(nums)
    while start < end:
        mid = start + (end - start) // 2
        if target >= nums[mid]:
            start = mid + 1
        elif target < nums[mid]:
            end = mid
    return start


print (searchLeftBoundary([1,3,3,3,5,7],4))
print (searchLeftBoundary([1,3,3,3,5,7],3))
print (searchLeftBoundary([3],3))
print (searchLeftBoundary([2],3))
print (searchLeftBoundary([4],3))

print (searchRightBoundary([1,3,3,3,5,7],4))
print (searchRightBoundary([1,3,3,3,5,7],3))
print (searchRightBoundary([3],3))
print (searchRightBoundary([2],3))
print (searchRightBoundary([4],3))
print (searchRightBoundary([],3))

# [1,3,3,3,5,7], target = 4 will return 1 (2nd element)
#     [1,3,3,3,5,7], target = 3 will return 1 (2nd element)
#     [3], target = 3 will return 0 (1st element)
#     [2], target = 3 will return 0 (1st element)
#     [4], target = 3 will return 1 (an out of bound element, as such a boundary does not exist)

#
# s=[1,2,3,4,5,6,7]
# print (binarySearch(0,len(s)-1,s,5))
# s=[1,2,3,4,5]
# print (binarySearch(0,len(s)-1,s,5))
# s=[1,5,1]
# print (binarySearch(0,len(s)-1,s,5))
# s=[5]
# print (binarySearch(0,len(s)-1,s,5))
# s=[5,1]
# print (binarySearch(0,len(s)-1,s,5))
# s=[1,5]
# print (binarySearch(0,len(s)-1,s,5))
#
# s=[1,2,3]
# print (binarySearch(0,len(s)-1,s,5))
# s=[1]
# print (binarySearch(0,len(s)-1,s,5))
# s=[]
# print (binarySearch(0,len(s)-1,s,5))