class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        s=0
        n=len(nums)
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                s+=nums[i-1]**2
                if i**2!=n:
                    s+=nums[(n//i)-1]**2
        return s
        