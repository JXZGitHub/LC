class Solution:
    """
    Area between 2 heights is at most width * smaller of the 2 heights.

    Two pointer: Starts at 2 ends. Compute area as width * shorter height.
    Then any larger area can only be found with the longer height. So adjust the smaller height inwards

    Time: O(N)
    Space: O(1)
    """
    def maxArea(self, height) -> int:
        start,end=0,len(height)-1
        area = 0
        while start < end:
            width = end-start
            start_h = height[start]
            end_h = height[end]
            area = max(area, width*min(start_h,end_h))
            if start_h < end_h:
                start +=1
            else:
                end -=1
        return area

class Solution2:
    """
    Small optimization: keep skipping heights that are <= the previous min height.
    """
    def maxArea(self, height):
        start, end = 0, len(height) - 1
        area = 0
        min_h = float('-inf')
        while start < end:
            start_h = height[start]
            end_h = height[end]

            #keep skipping heights that are <= the previous min height.
            if start_h <= min_h:
                start += 1
            elif end_h <= min_h:
                end -= 1
            else:
                width = end - start
                min_h = min(start_h, end_h)
                area = max(area, width * min_h)
        return area