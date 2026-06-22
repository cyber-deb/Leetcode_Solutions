class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s=set(allowed)
        c=0
        for i in words:
            if set(i).issubset(s):
                c+=1
        return c
        