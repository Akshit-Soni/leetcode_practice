class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = list(set(nums))
        a.sort()
        if len(a) >= 3:
            return a[-3]
        else:
            return a[-1]