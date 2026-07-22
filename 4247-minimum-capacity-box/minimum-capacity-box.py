class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        m=float("inf")
        index=-1
        for i,n in enumerate(capacity):
            if itemSize<=n<m:
                m=n
                index=i
        return index



