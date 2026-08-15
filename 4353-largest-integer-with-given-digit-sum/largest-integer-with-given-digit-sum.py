class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s>9*n:
            return -1
        if s==0:
            return 0
        ans=''
        for _ in range(n):
            x=min(9,s)
            ans+=str(x)
            s-=x
        return int(ans)