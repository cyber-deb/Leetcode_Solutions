class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        nig=[]
        ans=[]
        for i in nums:
            if i<0:
                nig.append(i)
            else:
                pos.append(i)
        for a,b in zip(pos,nig):
            ans.append(a)
            ans.append(b)
        return ans