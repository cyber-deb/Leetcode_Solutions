class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        l=sentence.split()
        s=''
        for i in range(len(l)):
            if l[i][0] in "AEIOUaeiou":
                s+=l[i]
            else:
                s+=(l[i][1:])+l[i][0]
            s+="ma"+("a"*(i+1))+' '
        return s[:-1]