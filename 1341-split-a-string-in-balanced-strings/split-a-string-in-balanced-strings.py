class Solution:
    def balancedStringSplit(self, s: str) -> int:
        lc=0
        rc=0
        n=0
        for i in s:
            if i=='L':
                lc+=1
            elif i=='R':
                rc+=1
            if lc==rc:
                n+=1
                lc,rc=0,0
        return n
            
        