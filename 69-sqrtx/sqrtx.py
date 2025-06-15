class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while x > 0:
            x = x - (2 * i + 1)
            i += 1
        if x < 0:
            return i - 1
        else:
            return i