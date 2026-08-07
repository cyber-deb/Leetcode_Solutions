class Solution:
    def matrixReshape(self,mat:List[List[int]],r:int,c:int)->List[List[int]]:
        if len(mat)*len(mat[0])!=r*c:
            return mat
        arr=[]
        for row in mat:
            arr.extend(row)
        ans=[]
        for i in range(0,len(arr),c):
            ans.append(arr[i:i+c])
        return ans