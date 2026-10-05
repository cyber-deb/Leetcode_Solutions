from collections import Counter
class Solution:
    def equalFrequency(self, word: str) -> bool:
        c=Counter(word)
        for x in list(c):
            c[x]-=1
            if c[x]==0:
                del c[x]
            if len(set(c.values()))==1:
                return True
            c=Counter(word)
        return False
        
        