class Solution:
    def countValidWords(self,sentence:str)->int:
        ans=0
        for w in sentence.split():
            if any(c.isdigit() for c in w):
                continue
            if w.count('-')>1:
                continue
            if '-' in w:
                i=w.index('-')
                if i==0 or i==len(w)-1 or not w[i-1].islower() or not w[i+1].islower():
                    continue
            p=sum(c in '!.,' for c in w)
            if p>1:
                continue
            if p and w[-1] not in '!.,':
                continue
            ans+=1
        return ans