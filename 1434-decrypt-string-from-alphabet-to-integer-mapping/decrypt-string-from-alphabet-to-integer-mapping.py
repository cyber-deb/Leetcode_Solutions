class Solution:
    def freqAlphabets(self, s: str) -> str:
        r=''
        i=0
        while i<len(s):
            if i+2<len(s) and s[i+2]=='#':
                r+=chr(96+int(s[i:i+2]))
                i+=2
            else:
                r+=chr(96+int(s[i]))
            i+=1
        return r
        