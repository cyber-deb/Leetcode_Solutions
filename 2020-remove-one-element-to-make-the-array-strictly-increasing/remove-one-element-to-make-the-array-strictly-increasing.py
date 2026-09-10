class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        c=0
        w=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<=w:
                c+=1
                if c>1:
                    return False
                if i>1 and nums[i]<=nums[i-2]:
                    continue
            w=nums[i]
        return True