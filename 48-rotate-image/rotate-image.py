class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ''' 0,0 -> 0,2
        0,1->1,2
        0,2->2,2
        1,0->0,1
        1,1->1,1
        1,2->2,1
        2,0->0,0
        2,1->1,0
        2,2->2,0'''
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for k in matrix:
            k.reverse()
        