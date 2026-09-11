class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        res=[]
        for i in drones:
            d=abs(target[0]-i[0])+abs(target[1]-i[1])
            if d>i[2]:
                res.append(101)
            else:
                res.append(d)
        return -1 if set(res)=={101} else res.index(min(res))
        