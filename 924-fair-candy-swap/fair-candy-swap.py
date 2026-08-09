class Solution:
    def fairCandySwap(self,aliceSizes:List[int],bobSizes:List[int])->List[int]:
        a=sum(aliceSizes)
        b=sum(bobSizes)
        d=(a-b)//2
        s=set(bobSizes)
        for x in aliceSizes:
            if x-d in s:
                return [x,x-d]