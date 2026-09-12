class Solution:
    def maxSum(self, nums: List[int]) -> int:
        x=set(nums)
        p=[i for i in x if i>0]
        return sum(p) if p else max(nums)
        