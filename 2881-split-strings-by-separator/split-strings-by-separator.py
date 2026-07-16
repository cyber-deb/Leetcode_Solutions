class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        l=[]
        for i in words:
            k=i.split(separator)
            while "" in k:
                k.remove("")
            for j in k:
                l.append(j)
        return l
        