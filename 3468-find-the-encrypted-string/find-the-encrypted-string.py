class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        ans=''
        l=len(s)
        for i in range(l):
            ans+=s[(i+k)%l]
        return ans