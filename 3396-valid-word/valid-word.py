class Solution:
    def isValid(self, word: str) -> bool:
        if (len(word)<3 or not any(c in 'aeiouAEIOU' for c in word) or not any(c.isalpha() and c not in 'aeiouAEIOU' for c in word) or not all(c.isalnum() for c in word)):
            return False
        return True