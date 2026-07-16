class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        d={}
        for x in nums:
            d[x]=d.get(x,0)+1
        left=0
        right=len(nums)
        ans=0
        for f in d.values():
            right-=f
            ans+=left*f*right
            left+=f
        return ans
        