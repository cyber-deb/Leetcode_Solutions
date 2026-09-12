from math import prod
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            if prod(list(map(int,str(n))))%t==0:
                return n
            else:
                n+=1
    
        