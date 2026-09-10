from datetime import date
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
            a=date.fromisoformat(date1)
            b=date.fromisoformat(date2)
            return abs((b-a).days)