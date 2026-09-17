class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for x in letters:
            if x>target:
                return x
        return letters[0]