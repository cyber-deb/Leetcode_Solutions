class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        s=0
        for row in grid:
            row.sort()
        for j in range(len(grid[0])):
            s+=max(row.pop() for row in grid)
        return s


        