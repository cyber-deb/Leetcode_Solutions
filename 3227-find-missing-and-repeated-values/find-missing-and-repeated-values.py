class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        c=[0]*(n*n+1)
        ans=[0]*2
        for row in grid:
            for i in row:
                c[i]+=1
        for i in range(1,n*n+1):
            if c[i]==2:
                ans[0]=i
            elif c[i]==0:
                ans[1]=i
        return ans