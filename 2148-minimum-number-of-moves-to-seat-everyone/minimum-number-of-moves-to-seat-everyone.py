class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        c=0
        for i in range(len(seats)):
            c+=abs(max(students)-max(seats))
            students.remove(max(students))
            seats.remove(max(seats))
        return c
        