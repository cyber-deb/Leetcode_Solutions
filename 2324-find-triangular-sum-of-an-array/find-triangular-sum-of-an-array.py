class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        k=[]
        while len(nums)!=1:
            for i in range(len(nums)-1):
                k.append((nums[i]+nums[i+1])%10)
            nums=k
            k=[]
        return nums[0]