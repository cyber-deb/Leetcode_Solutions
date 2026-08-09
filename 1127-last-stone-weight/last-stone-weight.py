class Solution:
    def lastStoneWeight(self,stones:List[int])->int:
        stones.sort()
        while len(stones)>1:
            m=stones.pop()-stones.pop()
            if m:
                stones.append(m)
                stones.sort()
        return stones[0] if stones else 0