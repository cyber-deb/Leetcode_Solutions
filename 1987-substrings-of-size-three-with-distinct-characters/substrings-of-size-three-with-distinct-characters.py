class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c=0
        for i in range(len(s)-2):
            if len(s[i:i+3])==len(set(s[i:i+3])):
                c+=1
        return c
            
        