class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            l.append(len(set(nums[0:i+1]))-len(set(nums[i+1:])))
        return l
        