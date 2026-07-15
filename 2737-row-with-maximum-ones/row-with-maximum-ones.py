class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        counts=[row.count(1) for row in mat]
        m=max(counts)
        return [counts.index(m),m]
        