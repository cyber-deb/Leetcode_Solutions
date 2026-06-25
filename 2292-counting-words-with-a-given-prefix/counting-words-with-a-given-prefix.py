class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        s=len(pref)
        c=0
        for i in words:
            if i[:s]==pref:
                c+=1
        return c
        