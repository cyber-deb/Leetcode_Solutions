class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat[0])
        s=0
        for i,j in zip(range(n),range(n)):
            s+=mat[i][j]
        for i,j in zip(range(n),range(n-1,-1,-1)):
            s+=mat[i][j]
        if n%2==1:
            return s-mat[n//2][n//2]
        return s

        