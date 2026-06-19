class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in set(arr):
            d[i]=arr.count(i)
        return len(d.values())==len(set(d.values()))
        