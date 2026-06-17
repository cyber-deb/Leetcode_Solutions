class Solution:
    def sortSentence(self, s: str) -> str:
        l=s.split()
        k=['']*len(l)
        for i in l:
            k[int(i[-1])-1]=i[:-1]
        return ' '.join(k)

        