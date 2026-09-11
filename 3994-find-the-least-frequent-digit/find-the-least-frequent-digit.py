class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        s=sorted(list(str(n)),key=lambda x:(str(n).count(x),int(x)))
        return int(s[0])