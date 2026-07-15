class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s=sum(apple)
        capacity.sort()
        t,c=0,0
        while t<s:
            t+=capacity.pop()
            c+=1
        return c
        