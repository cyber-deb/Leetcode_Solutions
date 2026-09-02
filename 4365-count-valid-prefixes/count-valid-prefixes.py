class Solution:
    def countValidPrefixes(self, s: str) -> int:
        c=1
        for i in range(1,len(s)):
            p=s[:i+1]
            z=str(p).count('0')
            o=str(p).count('1')
            if abs(z-o)<=1:
                c+=1
        return c