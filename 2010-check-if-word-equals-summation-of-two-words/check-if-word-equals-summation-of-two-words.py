class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        f,s,t=0,0,0
        for i in firstWord:
            f=f*10+(ord(i)-ord('a'))
        for i in secondWord:
            s=s*10+(ord(i)-ord('a'))
        for i in targetWord:
            t=t*10+(ord(i)-ord('a'))
        return t==(f+s)
        

        