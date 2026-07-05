class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        ans = 0
        for i,x in enumerate(nums):
            if i%2==0:
                ans+=x
            else:
                ans-=x
        return ans
        



        