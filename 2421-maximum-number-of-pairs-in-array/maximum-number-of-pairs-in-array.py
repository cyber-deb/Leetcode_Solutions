class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        pairs,leftover=0,0
        for i in d.values():
            pairs+=(i//2)
            leftover+=(i%2)
        return [pairs,leftover]