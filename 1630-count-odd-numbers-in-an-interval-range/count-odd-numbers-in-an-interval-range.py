class Solution:
    def countOdds(self, low: int, high: int) -> int:
        c=0
        if low%2!=0 or high%2!=0:
            c+=1
        return c+(high-low)//2
        