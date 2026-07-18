class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        pos={num:x for x,num in enumerate(order)}
        friends.sort(key=lambda x:pos[x])
        return friends
        