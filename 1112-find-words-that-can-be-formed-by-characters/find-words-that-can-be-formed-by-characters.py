from collections import Counter
class Solution:
    def countCharacters(self,words:List[str],chars:str)->int:
        c=Counter(chars)
        ans=0
        for word in words:
            w=Counter(word)
            if all(w[x]<=c[x] for x in w):
                ans+=len(word)
        return ans