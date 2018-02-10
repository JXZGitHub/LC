class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftIndex=0
        rightIndex=len(height)-1
        maxArea = 0
        while (leftIndex<rightIndex):
            maxArea = max(maxArea,
                          min(height[leftIndex],height[rightIndex]) * (rightIndex-leftIndex))

            #Keep the longer boundary as the area, and move the shorter boundary inward to see if there might be a longer boundary in the future.
            if height[leftIndex]>height[rightIndex]:
                rightIndex -= 1
            else:
                #If both boundaries are equal, doesn't matter which one to move inward.
                leftIndex += 1
        return maxArea
s=Solution()
print (s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print (s.maxArea([1,3,2,5,25,24,5]))
print (s.maxArea([3, 8]))
print (s.maxArea([3, 3]))