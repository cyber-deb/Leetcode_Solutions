class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res=[]
        for i in arr2:
            c=arr1.count(i)
            res+=[i]*c
            for j in range(c):
                arr1.remove(i)
        return res+sorted(arr1)