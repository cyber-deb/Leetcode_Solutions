class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        if len(nums)==1:
            return nums
        valid=[nums[0]]
        for i in range(1,len(nums)-1):
            if nums[i]>max(nums[:i]) or nums[i]>max(nums[i+1:]):
                valid.append(nums[i])
        valid.append(nums[-1])
        return valid