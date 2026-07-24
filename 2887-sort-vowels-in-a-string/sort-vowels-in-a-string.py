class Solution:
    def sortVowels(self, s: str) -> str:
        v="aeiouAEIOU"
        vow=[]
        for i in s:
            if i in v:
                vow.append(i)
        vow.sort()
        r=''
        j=0
        for i in s:
            if i in v:
                r+=vow[j]
                j+=1
            else:
                r+=i
        return r
        
        