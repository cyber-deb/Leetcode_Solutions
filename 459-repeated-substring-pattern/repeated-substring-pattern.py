class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1,len(s)//2+1):
            if len(s)%i!=0:
                continue
            k=0
            m=set()
            while k+i<=len(s):
                m.add(s[k:k+i])
                k+=i
            if len(m)==1:
                return True
        return False
