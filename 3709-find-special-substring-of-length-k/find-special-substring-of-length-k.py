class Solution:
    def hasSpecialSubstring(self,s:str,k:int)->bool:
        for i in range(len(s)-k+1):
            x=s[i:i+k]
            if len(set(x))==1:
                if i>0 and s[i-1]==x[0]:
                    continue
                if i+k<len(s) and s[i+k]==x[0]:
                    continue
                return True
        return False