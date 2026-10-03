class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        ans=[]
        rem=0
        for x in nums:
            rem=(rem*2+x)%5
            ans.append(rem==0)
        return ans
        