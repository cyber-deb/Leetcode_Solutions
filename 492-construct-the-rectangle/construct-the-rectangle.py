class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        k=int(area**0.5)
        if k*k==area:
            return [k,k]
        else:
            while True:
                m=area//k
                if m*k==area:
                    l,b=max(m,k),min(m,k)
                    return [l,b]
                k-=1
        
        