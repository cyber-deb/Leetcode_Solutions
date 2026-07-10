class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        c=0
        total=0
        for row in boxTypes:
            take=min(row[0],truckSize-total)
            total += take
            c+=row[1]*take
            if total==truckSize:
                break
        return c
        