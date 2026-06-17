class Solution:
    def replaceDigits(self, s: str) -> str:
        l=list(s)
        for i in range(1,len(s),2):
            l[i]=chr(ord(s[i-1])+int(s[i]))
        return ''.join(l)
        