class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        k=set(word.lower())
        c=0
        for i in k:
            if i.upper() in word and i in word:
                c+=1
        return c
        