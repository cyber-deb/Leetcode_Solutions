class Solution:
    def countPoints(self, rings: str) -> int:
        r=set()
        b=set()
        g=set()
        for i in range(0,len(rings),2):
            if rings[i]=='R':
                r.add(int(rings[i+1]))
            elif rings[i]=='G':
                g.add(int(rings[i+1]))
            else:
                b.add(int(rings[i+1]))
        return len(r&g&b)
        