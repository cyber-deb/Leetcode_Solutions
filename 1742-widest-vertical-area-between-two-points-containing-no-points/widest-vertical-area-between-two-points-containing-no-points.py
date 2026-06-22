class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x=sorted(p[0] for p in points)
        ans=0
        for i in range(len(x)-1):
            ans=max(ans,x[i + 1]-x[i])
        return ans