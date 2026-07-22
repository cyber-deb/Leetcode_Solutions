class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        if m == 1:
            return ["." * n]
        if n == 1:
            return ["." for _ in range(m)]
        grid = [["#"] * n for _ in range(m)]
        for j in range(n - 1):
            grid[0][j] = "."
        for i in range(1, m):
            grid[i][n - 2] = "."
        grid[m - 1][n - 1] = "."
        return ["".join(row) for row in grid]