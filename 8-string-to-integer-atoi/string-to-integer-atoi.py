class Solution:
    def myAtoi(self, s: str) -> int:
        c,k=0,0
        s=s.strip()
        if s=='':
            return 0
        if s[0] not in {'+','-'}:
            s='+'+s
        for i in s[1::]:
            if i.isdigit()==False:
                break
            c=c*10+int(i)
        c=c if s[0]=='+' else c*(-1)
        if c > 2**31 - 1:
            return 2**31 - 1
        if c < -2**31:
            return -2**31
        return c  