from collections import Counter
class Solution:
    def shortestCompletingWord(self,licensePlate:str,words:List[str])->str:
        need=Counter(c.lower() for c in licensePlate if c.isalpha())
        for word in sorted(words,key=len):
            have=Counter(word)
            if all(have[c]>=need[c] for c in need):
                return word
        