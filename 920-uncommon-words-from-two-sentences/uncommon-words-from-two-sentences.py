class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d={}
        for word in (s1+" "+s2).split():
            d[word]=d.get(word,0)+1
        return [word for word, cnt in d.items() if cnt==1]