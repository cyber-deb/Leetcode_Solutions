class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        c=0
        for i in range (len(s)):
            if s[0:i+1] in words:
                c+=words.count(s[0:i+1])
        return c