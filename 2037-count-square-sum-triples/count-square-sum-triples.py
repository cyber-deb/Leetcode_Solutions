class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for a in range(1,n+1):
            for b in range(1,n+1):
                s=a*a+b*b
                if s>n*n:
                    break
                c=int(s**0.5)
                if c*c==s:
                    count+=1
        return count