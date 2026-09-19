class Solution:
    def canAliceWin(self, n: int) -> bool:
        c=0
        k=10
        while n-k>=0:
            n-=k
            k-=1
            c+=1
        return True if c%2==1 else False
        