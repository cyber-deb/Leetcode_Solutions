from math import comb as c
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n=len(nums)
        s=0
        for i in range(n):
            s+=nums[i]*c(n-1,i)
        return s%10