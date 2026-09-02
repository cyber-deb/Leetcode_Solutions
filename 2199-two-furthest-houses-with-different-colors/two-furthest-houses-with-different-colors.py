class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n=len(colors)
        ans=0
        for i in range(n-1,-1,-1):
            if colors[0]!=colors[i]:
                ans=max(ans,i)
                break
        for i in range(n):
            if colors[-1]!=colors[i]:
                ans=max(ans,n-1-i)
                break
        return ans