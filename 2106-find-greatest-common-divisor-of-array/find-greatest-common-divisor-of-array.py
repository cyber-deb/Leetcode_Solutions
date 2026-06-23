class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=max(nums)
        b=min(nums)
        rem=b
        while b!=0:
            rem=a%b
            a,b=b,rem
        return a
        