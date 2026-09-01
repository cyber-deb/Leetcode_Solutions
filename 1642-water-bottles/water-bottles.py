class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans=numBottles
        empty=numBottles
        while empty>=numExchange:
            new=empty//numExchange
            empty=empty%numExchange+new
            ans+=new
        return ans
            
