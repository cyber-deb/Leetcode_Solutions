class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        c=[]
        for i in matrix:
            c.append(i.count(1))
        return c
        