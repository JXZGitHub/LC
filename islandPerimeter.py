class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        Time: O(R*C)
        Space: O(1)
        
        Starts by 'adding' borders around grid that are all 0's, then start at the enlarged grid, for any 0, count any 1's that are neighboring it.
        """                
        peri = 0
        for r in range(-1,len(grid)+1):
            for c in range(-1,len(grid[0])+1):
                if r==-1 or r==len(grid) or c==-1 or c==len(grid[0]) or grid[r][c] == 0: 
                    for d in [(1,0),(-1,0),(0,1),(0,-1)]:
                        newR,newC= r+d[0], c+d[1]
                        if 0<=newR<len(grid) and 0<=newC<len(grid[0]) and grid[newR][newC]==1:
                            peri +=1                
        return peri                  
                            
