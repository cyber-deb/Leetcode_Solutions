class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n=len(grid)
        for i in range(n):
            champion=True
            for j in range(n):
                if grid[j][i]==1:
                    champion=False
                    break
            if champion:
                return i
        