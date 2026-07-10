class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d={}
        for i in range(len(mat)):
            d[i]=mat[i].count(1)
        return sorted(d,key=d.get)[:k]
        