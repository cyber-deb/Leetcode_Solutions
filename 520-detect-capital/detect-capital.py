class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.upper()==word or word.lower()==word or (sum(x.isupper() for x in word)==1 and word[0].isupper())