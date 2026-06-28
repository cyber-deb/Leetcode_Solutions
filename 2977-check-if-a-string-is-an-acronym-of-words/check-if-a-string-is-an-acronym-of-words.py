class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words)!=len(s):
            return False
        k=''
        for i in words:
            k+=i[0]
        return k==s
        