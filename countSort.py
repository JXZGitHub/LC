from collections import defaultdict
def count_sort(input, minV, maxV):
    """ Input: a lits of integers, whose values range from [minV, maxV]
        Count sort is a good sorting algorithm if maxV - minV is significantly smaller than the length of the input.
        eg: Sort a million integers (0-9).

        Time: O(n+k). n is size of input, k is size of maxV-minV
        Space: O(n+k)
    """
    count = defaultdict(int)
    output = [ None for i in range(len(input))]
    for i in input:
        count[i] += 1
    total = 0
    for k in range(minV,maxV+1):
        prev_count = count[k]
        count[k] = total
        total += prev_count
    for i in input:
        output[ count[i] ] = i
        count[i] += 1
    return output

print (count_sort([1,4,1,2,7,5,2],0,9))
