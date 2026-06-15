class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        def alpha(x):
            if x == 0:
                return ""
            x -= 1
            divisor = x // 26
            remainder = x % 26
            return alpha(divisor) + chr(ord('A') + remainder)
        return alpha(columnNumber)
        

        