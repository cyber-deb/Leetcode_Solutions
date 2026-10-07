class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        c=0
        for i in set(nums):
            k=nums.index(i)
            m=nums.count(i)
            if len(set(nums[k:k+m]))==1:
                c+=1
        return c
        