class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n=0
        while n<len(nums) and nums[n]<0:
            n+=1
        z=nums.count(0)
        p=len(nums)-n-z
        return max(p,n)