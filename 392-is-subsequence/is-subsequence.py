class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        o=0
        for i in s:
            index=t[o:].find(i)
            if index==-1:
                return False
            else:
                o+=index+1
        return True