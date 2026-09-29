class Solution:
    def countEven(self, num: int) -> int:
        c=0
        for i in range(1,num+1):
            s=sum(int(x) for x in list(str(i)))%2==0
            if s:
                c+=1
        return c
        