class Solution:
    def reformat(self, s: str) -> str:
        l=[x for x in s if x.isalpha()]
        d=[x for x in s if x.isdigit()]
        if abs(len(l)-len(d))>1:
            return ""
        s=''
        for i,j in zip(l,d):
            s+=i+j
        if len(l)>len(d):
            s+=l[-1]
        elif len(d)>len(l):
            s=d[-1]+s
        return s
            