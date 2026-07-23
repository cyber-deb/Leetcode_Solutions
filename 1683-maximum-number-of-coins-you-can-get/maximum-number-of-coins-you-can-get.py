class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        ans=0
        rounds=len(piles)//3
        for i in range(1,2*rounds,2):
            ans+=piles[i]
        return ans