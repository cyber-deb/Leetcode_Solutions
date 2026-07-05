class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=int(bin(nums[i])[-1])
        return sorted(nums)