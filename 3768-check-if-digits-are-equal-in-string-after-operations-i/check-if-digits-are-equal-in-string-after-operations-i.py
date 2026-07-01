class Solution:
    def hasSameDigits(self, s: str) -> bool:
        i=0
        k=''
        while len(s)!=2:
            for i in range(len(s)-1):
                k+=str((int(s[i])+int(s[i+1]))%10)
            s=k
            k=''
        return s[0]==s[1]

        