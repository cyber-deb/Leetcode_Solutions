class Solution:
    def trailingZeroes(self, n: int) -> int:
        c=0
        k=5
        while n>=k:
            c=c+n//k
            k*=5
        return c
        