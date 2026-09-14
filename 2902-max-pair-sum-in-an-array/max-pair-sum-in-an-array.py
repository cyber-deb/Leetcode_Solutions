class Solution:
    def maxSum(self, nums: List[int]) -> int:
        d={}
        ans=-1
        for n in nums:
            x=max(map(int,str(n)))
            if x in d:
                ans=max(ans,n+d[x])
                d[x]=max(d[x],n)
            else:
                d[x]=n
        return ans