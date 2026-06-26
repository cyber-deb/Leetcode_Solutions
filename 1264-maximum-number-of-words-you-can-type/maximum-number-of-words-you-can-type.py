class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l=text.split()
        c=0
        for i in l:
            if set(brokenLetters).isdisjoint(set(i)):
                c+=1
        return c




        