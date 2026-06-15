class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        c = list(columnTitle)
        c.reverse()
        k=0
        for i in range(len(c)):
            k=k+((ord(c[i])-64)*(26)**i)
        return k
        