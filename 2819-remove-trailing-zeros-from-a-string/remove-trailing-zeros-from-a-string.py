class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        for i in range(len(num)):
            if num[-1]=='0':
                num=num[:-1]
        return num