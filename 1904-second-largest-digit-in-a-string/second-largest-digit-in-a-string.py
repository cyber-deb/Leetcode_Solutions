class Solution:
    def secondHighest(self, s: str) -> int:
        d=sorted(set(int(x) for x in s if x.isdigit()))
        return d[-2] if len(d)>=2 else -1