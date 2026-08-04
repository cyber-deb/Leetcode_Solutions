class Solution:
    def surfaceArea(self,grid:List[List[int]])->int:
        ans=0
        n=len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    ans+=2
                    ans+=max(0,grid[i][j]-(grid[i-1][j] if i>0 else 0))
                    ans+=max(0,grid[i][j]-(grid[i+1][j] if i<n-1 else 0))
                    ans+=max(0,grid[i][j]-(grid[i][j-1] if j>0 else 0))
                    ans+=max(0,grid[i][j]-(grid[i][j+1] if j<n-1 else 0))
        return ans