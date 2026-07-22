class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        o=[]
        for i in bulbs:
            if i in o:
                o.remove(i)
            else:
                o.append(i)
        return sorted(o)