class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i,j=0,0
        for k in commands:
            if k=='LEFT':
                j-=1
            elif k=='RIGHT':
                j+=1
            elif k=='UP':
                i+=1
            else:
                i-=1
        return abs(i*n)+abs(j)
        