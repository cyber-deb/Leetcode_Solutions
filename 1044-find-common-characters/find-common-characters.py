class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c=[float('inf')]*26
        for word in words:
            freq=[0]*26
            for ch in word:
                freq[ord(ch)-ord('a')]+=1
            for i in range(26):
                c[i]=min(c[i],freq[i])
        ans=[]
        for i in range(26):
            ans.extend([chr(i + ord('a'))] * c[i])
        return ans