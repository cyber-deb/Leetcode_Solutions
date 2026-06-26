class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s,d=0,0
        for i in nums:
            s+=i
            d+=i%10
            while i//10!=0:
                i//=10
                d+=i%10
        return abs(s-d)

