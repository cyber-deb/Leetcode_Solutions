class Solution:
    def greatestLetter(self, s: str) -> str:
        for ch in "ZYXWVUTSRQPONMLKJIHGFEDCBA":
            if ch in s and ch.lower() in s:
                return ch
        return ""