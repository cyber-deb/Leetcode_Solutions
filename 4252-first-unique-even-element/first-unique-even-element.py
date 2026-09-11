from collections import Counter
class Solution:
    def firstUniqueEven(self,nums:List[int])->int:
        c=Counter(nums)
        return next((x for x in nums if x%2==0 and c[x]==1),-1)