class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        l=list(map(int,str(n)))
        return sum(l)
        