class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        k='abcdefghijklmnopqrstuvwxyz'
        d={}
        for i, j in zip(k, weights):
            d[i] = j
        ans = ''
        for i in words:
            r=0
            for j in i:
                r+=d[j]
            r %= 26
            ans += chr(ord('z') - r)
        return ans
        