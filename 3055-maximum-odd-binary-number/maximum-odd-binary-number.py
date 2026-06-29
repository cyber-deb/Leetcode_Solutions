class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        l=list(s)
        l.remove('1')
        l.append('1')
        c=l.count('1')-1
        if c==0:
            return ''.join(l)
        for i in range (c):
            l.remove('1')
        return '1'*c+''.join(l)