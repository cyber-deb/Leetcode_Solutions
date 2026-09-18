class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        l=[0,1]
        for i in range(2,n+1):
            if i%2==0:
                l.append(l[i//2])
            else:
                l.append(l[i//2]+l[(i//2)+1])
        return max(l)