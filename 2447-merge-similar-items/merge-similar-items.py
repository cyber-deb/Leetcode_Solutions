class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d={}
        for i in items1:
            d[i[0]]=d.get(i[0],0)+i[1]
        for i in items2:
            d[i[0]]=d.get(i[0],0)+i[1]
        return sorted([[k,d[k]] for k in d.keys()])
        