class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        c=0
        r=0
        for i in set(s):
            k=s.count(i)
            if k==1 and c!=1:
                r+=1
                c+=1
            if k%2!=0 and k!=1:
                r+=k-1
                if c!=1:
                    r+=1
                    c+=1
            elif k%2==0:
                r+=k
        return r

            