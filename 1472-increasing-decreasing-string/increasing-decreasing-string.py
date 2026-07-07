class Solution:
    def sortString(self, s: str) -> str:
        d = {}
        for i in s:
            d[i]=d.get(i,0)+1
        ans = ""
        while len(ans)<len(s):
            for ch in sorted(d):
                if d[ch]>0:
                    ans+=ch
                    d[ch]-=1
            for ch in sorted(d,reverse=True):
                if d[ch]>0:
                    ans+=ch
                    d[ch]-=1
        return ans

        