class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        c=0
        s=0
        for i in nums:
            s+=i
            c+=(s==0)
        return c

        