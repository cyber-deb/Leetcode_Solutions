from math import factorial as fact
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        p=0
        for x in range(2,n+1):
            prime=True
            for i in range(2,int(x**0.5)+1):
                if x%i==0:
                    prime=False
                    break
            if prime:
                p+=1
        return (fact(p)*fact(n-p))%(10**9+7)
                