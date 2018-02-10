class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        #Water is only trapped if a given vlaue is LESS than its previous (left pointer's right one, and right pointer's left one)
        #So we keep 2 pointers, L and R. If left height is less than right height, keep moving from left, and as soon as a
        #value is less than the original minimum left, add the difference as a collected value. Same with right side.
        """
        l = 0
        r = len(height)-1
        res = 0
        while l < r:
            minH = min(height[l],height[r])
            if minH == height[l]:
                l+=1
                while (l<r and height[l] < minH):
                    res += (minH - height[l])
                    l+=1
            elif minH == height[r]:
                r-=1
                while (l<r and height[r] < minH):
                    res += (minH - height[r])
                    r-=1
        return res