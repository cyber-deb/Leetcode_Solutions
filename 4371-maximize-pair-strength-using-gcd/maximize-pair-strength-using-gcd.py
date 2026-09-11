from math import gcd
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        m=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                m=max(m,((nums[i]*nums[j])//(gcd(nums[i],nums[j])**2)))
        return m

        