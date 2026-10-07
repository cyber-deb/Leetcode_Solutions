class Solution:
    def minRotations(self, s: str) -> int:
        r=min(int(s[0]),abs(10-int(s[0])))
        for i in range (1,len(s)):
            chota,bada=min(int(s[i-1]),int(s[i])),max(int(s[i-1]),int(s[i]))
            r+=min(bada-chota,chota+10-bada)
        return r
