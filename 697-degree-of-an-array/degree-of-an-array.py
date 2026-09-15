from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        c=Counter(nums)
        d={}
        for i,x in enumerate(nums):
            if x not in d:
                d[x]=[i,i]
            else:
                d[x][1]=i
        degree=max(c.values())
        ans=len(nums)
        for x in c:
            if c[x]==degree:
                ans=min(ans,d[x][1]-d[x][0]+1)
        return ans