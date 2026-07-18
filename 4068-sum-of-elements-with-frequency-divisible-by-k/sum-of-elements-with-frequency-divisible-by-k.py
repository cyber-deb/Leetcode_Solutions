class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        s=0
        for i in d.keys():
            if d[i]%k==0:
                s+=(i*d[i])
        return s