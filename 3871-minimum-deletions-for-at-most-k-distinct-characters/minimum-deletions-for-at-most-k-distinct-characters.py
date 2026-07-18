class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        if len(set(s))<=k:
            return 0
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        c=0
        l=sorted(list(d.values()))
        while len(l)>k:
            c+=l.pop(0)
        return c 
        