class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        o=set()
        for i in bulbs:
            if i in o:
                o.remove(i)
            else:
                o.add(i)
        return sorted(o)