class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        s=sorted(set(nums),reverse=True)
        if len(s)<k:
            return list(s)
        else:
            return list(s[:k])

        