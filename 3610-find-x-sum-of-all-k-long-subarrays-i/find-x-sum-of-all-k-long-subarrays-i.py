class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        l=[]
        i=0
        while i+k<=len(nums):
            d={}
            for m in nums[i:i+k]:
                d[m]=d.get(m,0)+1
            keys=sorted(d,key=lambda x:(-d[x],-x))
            ans=0
            for j in keys[:x]:
                ans+=j*d[j]
            l.append(ans)
            i+=1
        return l