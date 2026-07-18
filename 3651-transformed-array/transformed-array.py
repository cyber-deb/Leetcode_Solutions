class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result=[]
        l=len(nums)
        for i in range(l):
            result.append(nums[(i+nums[i])%l])
        return result
        
        