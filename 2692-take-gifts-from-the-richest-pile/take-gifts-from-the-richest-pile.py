class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            o=max(gifts)
            gifts[gifts.index(o)]=int(o**0.5)
        return sum(gifts)
        