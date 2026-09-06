class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=0
        for i in range(len(str(n))):
            s=s+int(str(n)[i]) if i%2==0 else s-int(str(n)[i])
        return s