class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s=sorted(set(arr))
        d={x:i+1 for i,x in enumerate(s)}
        return [d[x] for x in arr]

        