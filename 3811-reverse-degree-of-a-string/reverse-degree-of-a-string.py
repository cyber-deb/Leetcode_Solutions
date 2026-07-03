class Solution:
    def reverseDegree(self, s: str) -> int:
        a=0
        for i in range(len(s)):
            a+=(123-ord(s[i]))*(i+1)
        return a
        