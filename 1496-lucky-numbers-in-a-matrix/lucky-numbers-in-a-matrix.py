class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        ans=[]
        for i in range(m):
            s=min(matrix[i])
            if max([matrix[k][matrix[i].index(s)] for k in range(m)])==s:
                ans.append(s)
        return ans
        