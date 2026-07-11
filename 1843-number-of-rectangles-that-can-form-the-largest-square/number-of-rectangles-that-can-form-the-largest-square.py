class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        s=[]
        for i in rectangles:
            s.append(min(i))
        return s.count(max(s))
        