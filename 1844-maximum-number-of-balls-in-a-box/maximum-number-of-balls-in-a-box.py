class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        if highLimit<9:
            return 1
        d={}
        for i in range(lowLimit,highLimit+1):
            s=sum(list(map(int,str(i))))
            d[s]=d.get(s,0)+1
        return max(d.values())

        