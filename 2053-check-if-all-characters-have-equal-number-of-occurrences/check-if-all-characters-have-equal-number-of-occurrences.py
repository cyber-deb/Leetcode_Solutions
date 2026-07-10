class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for i in set(s):
            d[i]=s.count(i)
        return len(set(d.values()))==1
        