class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = list(s.strip().split())
        return len(arr[-1])
