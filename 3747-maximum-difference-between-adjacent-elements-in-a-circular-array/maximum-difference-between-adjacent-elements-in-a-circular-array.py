class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        m=0
        for i in range(len(nums)):
            m=max(abs(nums[i]-nums[(i+1)%len(nums)]),m)
        return m
        