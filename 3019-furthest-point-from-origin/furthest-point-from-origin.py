class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l,r=moves.count('L'),moves.count('R')
        return moves.count('_')+abs(l-r)