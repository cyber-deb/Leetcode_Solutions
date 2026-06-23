class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        c=0
        for i in range(1, len(nums)):
            need=nums[i-1]+1-nums[i]
            if need>0:
                nums[i]+=need
                c+=need
        return c

        