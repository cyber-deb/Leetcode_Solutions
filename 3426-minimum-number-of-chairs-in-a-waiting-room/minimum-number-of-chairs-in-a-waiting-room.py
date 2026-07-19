class Solution:
    def minimumChairs(self, s: str) -> int:
        m=0
        c=0
        for i in s:
            c=c+1 if i=='E' else c-1
            m=max(c,m)
        return m
        