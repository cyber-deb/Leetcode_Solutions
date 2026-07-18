class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        c=0
        for i in range(n):
            k=grid[0][i]
            for  j in range(1,m):
                if grid[j][i]<=k:
                    c+=k+1-grid[j][i]
                    k+=1
                else:
                    k=grid[j][i]
        return c
        