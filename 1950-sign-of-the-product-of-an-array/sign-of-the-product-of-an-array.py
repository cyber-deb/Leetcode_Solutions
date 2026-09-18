class Solution:
    def arraySign(self, nums: list[int]) -> int:
        c=0
        for x in nums:
            if x==0:
                return 0
            if x<0:
                c+=1
        return -1 if c%2 else 1