class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        r=0
        for i in range(0,n,2):
            r+=min(nums[i:i+2])
        return r
