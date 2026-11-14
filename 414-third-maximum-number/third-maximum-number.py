class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        s=set(nums)
        if len(s)<3:
            return(max(s))
        else:
            k=sorted(s, reverse=True)
            return k[2]