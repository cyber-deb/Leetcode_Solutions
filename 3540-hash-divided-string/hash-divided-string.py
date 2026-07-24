class Solution:
    def stringHash(self, s: str, k: int) -> str:
        r=''
        for i in range(0,len(s),k):
            r+=chr(sum(ord(c)-97 for c in s[i:i+k])%26+97)
        return r