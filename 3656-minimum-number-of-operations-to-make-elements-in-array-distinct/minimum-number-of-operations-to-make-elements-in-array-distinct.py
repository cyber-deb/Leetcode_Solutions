class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c=0
        while True:
            if len(nums)==len(set(nums)):
                break
            else:
                nums=nums[3:]
                c+=1
        return c
        