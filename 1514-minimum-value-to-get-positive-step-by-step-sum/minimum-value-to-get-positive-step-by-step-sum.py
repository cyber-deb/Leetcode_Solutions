class Solution:
    def minStartValue(self,nums:List[int])->int:
        s=0
        mn=0
        for x in nums:
            s+=x
            mn=min(mn,s)
        return 1-mn