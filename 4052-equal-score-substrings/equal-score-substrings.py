class Solution:
    def scoreBalance(self,s:str)->bool:
        total=sum(ord(c)-96 for c in s)
        left=0
        for i in range(len(s)-1):
            left+=ord(s[i])-96
            if left==total-left:
                return True
        return False