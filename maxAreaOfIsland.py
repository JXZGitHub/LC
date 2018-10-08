class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxArea = 0
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxArea = max(self.traverse(r,c,grid,visited,0),maxArea)
        return maxArea
        
    def traverse(self,r,c,grid,visited,area):
        if not (0<=r<len(grid) and 0<=c<len(grid[0])) or grid[r][c] != 1 or (r,c) in visited:
            return 0            
        visited.add((r,c))
        area = 1
        for d in [(0,1),(0,-1),(-1,0),(1,0)]:
            newR,newC = r+d[0], c+d[1]            
            area += self.traverse(newR,newC,grid,visited,0)      
        return area
                
class Solution_BFS
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxArea = 0
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = 0
                    q = [(r,c)]
                    while q:            
                        newQ=[]
                        for r,c in q:   
                            if (r,c) not in visited:
                                area += 1
                                visited.add((r,c))
                                for d in [(0,1),(0,-1),(-1,0),(1,0)]:
                                    newR,newC = r+d[0], c+d[1]                            
                                    if 0<=newR<len(grid) and 0<=newC<len(grid[0]) and grid[newR][newC] == 1:   
                                        newQ.append((newR,newC))                                                                      
                        q=newQ
                    maxArea = max(area,maxArea)
        return maxArea             
                        
      
