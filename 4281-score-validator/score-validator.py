class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        s,c=0,0
        for i in events:
            if i in "0123456":
                s+=int(i)
            elif i in ["WD","NB"]:
                s+=1
            else:
                c+=1
            if c==10:
                break
        return [s,c]
        