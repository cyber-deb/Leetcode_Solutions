class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        a=''
        l,r=0,0
        start=1
        for i in range(len(s)):
            if s[i]=='(':
                l+=1
            else:
                r+=1
            if l==r:
                l,r=0,0
                a+=s[start:i]
                start=i+2
        return a

        