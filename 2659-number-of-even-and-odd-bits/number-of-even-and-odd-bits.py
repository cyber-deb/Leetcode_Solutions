class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        e,o=0,0
        b=reversed(bin(n)[2:])
        for i,j in enumerate(b):
            if j=='1':
                if i%2==0:
                    e+=1
                else:
                    o+=1
        return [e,o]
        