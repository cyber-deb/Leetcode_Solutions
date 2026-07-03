class Solution:
    def maxFreqSum(self, s: str) -> int:
        v='aeiou'
        vow=0
        cons=0
        for i in set(s):
            if i in v:
                vow=max(vow,s.count(i))
            else:
                cons=max(cons,s.count(i))
        return vow+cons        