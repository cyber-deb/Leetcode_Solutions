class Solution:
    def findLucky(self, arr: List[int]) -> int:
        m=-1
        for i in set(arr):
            if arr.count(i)==i:
                m=max(m,i)
        return m