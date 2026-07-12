class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans=[]
        freq={}
        for d in digits:
            freq[d]=freq.get(d,0)+1
        for num in range(100,1000,2):
            a=num//100
            b=(num//10)%10
            c=num%10
            need = {}
            for x in [a, b, c]:
                need[x] = need.get(x, 0) + 1
            ok = True
            for x in need:
                if freq.get(x, 0) < need[x]:
                    ok = False
                    break
            if ok:
                ans.append(num)
        return ans