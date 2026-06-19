class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        m=float("inf")
        ans=[]
        arr.sort()
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]<m:
                m=arr[i+1]-arr[i]
                ans=[[arr[i],arr[i+1]]]
            elif arr[i+1]-arr[i]==m:
                ans.append([arr[i],arr[i+1]])
        return ans
