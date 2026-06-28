class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c=0
        for i in range(low,high+1):
            if len(str(i))%2==0:
                n=len(str(i))//2
                s=str(i)
                if sum(map(int,s[:n]))==sum(map(int,s[n:])):
                    c+=1
        return c
        