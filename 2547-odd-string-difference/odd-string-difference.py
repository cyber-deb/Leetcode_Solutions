from collections import Counter
class Solution:
    def oddString(self,words:List[str])->str:
        d=[]
        for w in words:
            d.append(tuple(ord(w[i+1])-ord(w[i]) for i in range(len(w)-1)))
        c=Counter(d)
        for i in range(len(words)):
            if c[d[i]]==1:
                return words[i]