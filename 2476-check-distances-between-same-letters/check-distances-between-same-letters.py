class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        for i in set(s):
            d1=s.index(i)
            d2=s.index(i, d1 + 1)
            if d2-d1-1!=distance[ord(i)-97]:
                return False
        return True
        