class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        odd=0
        even=0
        n=len(nums)
        ans=[0]*n
        for i in range(n-1,-1,-1):
            if nums[i]%2==0:
                ans[i]=odd
                even+=1
            else:
                ans[i]=even
                odd+=1
        return ans