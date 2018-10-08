class Solution_DFS:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        
        Time: O(R*C)
        Space: O(max(len(image),len(image[0]))) on stack. O(R*C) on heap.
        """                
        currColor = image[sr][sc]
        if currColor == newColor:
            return image
        self.fill(image,sr,sc,currColor,newColor)
        return image
        
    def fill(self,image,r,c,currColor,newColor):        
        if 0<=r<len(image) and 0<=c<len(image[0]) and image[r][c]==currColor:
            image[r][c] = newColor            
            for d in [(1,0),(-1,0),(0,1),(0,-1)]:
                newR,newC = r+d[0],c+d[1]
                self.fill(image,newR,newC,currColor,newColor)
        
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        
        Time: O(R*C)
        Space: O(R*C)
        """        
        q = [(sr,sc)]
        currColor = image[sr][sc]  
        if currColor == newColor:
            return image
        while q:
            newQ=[]
            for r,c in q:                
                image[r][c] = newColor               
                for d in [(1,0),(-1,0),(0,1),(0,-1)]:
                    newR,newC = r+d[0],c+d[1]
                    if 0<=newR<len(image) and 0<=newC<len(image[0]) and image[newR][newC]==currColor:
                        newR,newC = r+d[0],c+d[1]
                        newQ.append((newR,newC))
            q=newQ
        return image                 
                
  
