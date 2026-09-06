class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        s=set()
        for i in range(len(nums)-1):
            k=nums[i]+nums[i+1]
            if k in s:
                return True
            s.add(k)
        return False
        