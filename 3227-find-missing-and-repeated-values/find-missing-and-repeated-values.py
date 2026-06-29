class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums=[]
        n=len(grid)
        for row in grid:
            nums.extend(row)
        repeat=0
        missing=0
        for i in range(1,n*n+1):
            if nums.count(i)==2:
                repeat=i
            elif nums.count(i)==0:
                missing=i
        return [repeat,missing]