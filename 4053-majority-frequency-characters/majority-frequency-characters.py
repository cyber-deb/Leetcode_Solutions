from collections import Counter
class Solution:
    def majorityFrequencyGroup(self,s:str)->str:
        c=Counter(s)
        g={}
        for x in c:
            g.setdefault(c[x],[]).append(x)
        k=max(g,key=lambda x:(len(g[x]),x))
        return ''.join(g[k])