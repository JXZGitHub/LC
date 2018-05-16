# Complete the getMinimumUniqueSum function below.
# For an array of numbers, make them all unique by incrementing any duplicate number, then return sum
# eg: [1,1,1] -> [1,2,3] (increment 1 to 2, then the last 1 to 3], sum is 6.

def getMinimumUniqueSum(arr):
    arr.sort()
    i = 1
    lastChanged = arr[0]
    while (i < len(arr)):
        if arr[i] <= lastChanged:
            arr[i] = lastChanged + 1
        lastChanged = arr[i]
        i += 1

    return sum(arr)

print (getMinimumUniqueSum([1,1,1]))